import csv, collections, datetime, json
P='/home/user/operaciones-planificacion-siembra-dcb/07-datos/'
C={c['grupo']:c for c in csv.DictReader(open(P+'ciclos_variedad.csv'))}
MAP=[('Lisianthus','Lisianthus'),('Snapdragon MB','Boca de Dragón MB'),('Snapdragon','Boca de Dragón'),
 ('Celosia Purple Flamingo','Celosia Purple Flamingo'),('Celosia Flamingo','Celosia Purple Flamingo'),
 ('Cristata','Celosia cristata'),('Celway','Celosia cristata'),('Celosia','Celosia plumosa'),
 ('Gomphrena','Gomphrena'),('Campanula','Campanula'),('Campánula','Campanula'),
 ('Trachellium','Trachellium'),('Trachelium','Trachellium'),('Matricaria','Matricaria'),
 ('Statice','Statice'),('Limonium','Limonium'),('Ammi','Ammi'),('Strawflower','Strawflower'),
 ('Strawfloer','Strawflower'),('Dusty Miller','Dusty Miller'),('Senecio','Dusty Miller'),
 ('Zinnia','Zinnia'),('Daucus','Daucus carota'),('Girasol','Girasol'),('Sunflower','Girasol'),
 ('Ammobium','Ammobium'),('Amaranto','Amaranto'),('Green Ball','Green Ball'),('Green ball','Green Ball'),
 ('Carthamus','Carthamus'),('Dianthus Green Ball','Green Ball'),('Dianthus','Dianthus'),
 ('Ptilotus','Ptilotus'),('Matildas','Ptilotus'),('Helipterum','Heliperum'),('Marigold','Marigold'),
 ('Achillea','Orlaya'),('Orlaya','Orlaya'),('Scabiosa','Scabiosa'),('Dahlia','Dahlia'),
 ('Larkspur','Larkspur'),('Anemona','Anémona'),('Ranunculus','Ranúnculo')]
def grupo(v):
    for k,g in MAP:
        if k.lower() in v.lower(): return g
    return ''
# el registro usa nombres de grupo propios -> homologar al grupo de ciclos
REG={'Boca de Dragón':'Boca de Dragón','Statice':'Statice','Gomphrena':'Gomphrena',
 'Celosia':'Celosia plumosa','Lisianthus':'Lisianthus','Zinnia':'Zinnia','Green Ball':'Green Ball',
 'Campanula':'Campanula','Ammi':'Ammi','Ammobium':'Ammobium','Amaranto':'Amaranto',
 'Strawflower':'Strawflower','Matricaria':'Matricaria','Girasol':'Girasol','Dusty Miller':'Dusty Miller',
 'Larkspur':'Larkspur','Trachellium':'Trachellium','Dahlias':'Dahlia','Amaranto velvet':'Amaranto'}

import re
def dig(v):
    n=re.findall(r'\d[\d.,]*',str(v))
    return sum(int(x.replace('.','').replace(',','')) for x in n) if n else 0

# ---------- denominador: plantas-semana en cosecha, por grupo ----------
rows=list(csv.reader(open('puente.csv')))[2:]
lot=[]
for r in rows:
    var=r[2].strip()
    if not var: continue
    g=grupo(var)
    if not g: continue
    try: ini=int(r[10])
    except: continue
    try: fin=int(r[11])
    except:
        vm=C.get(g,{}).get('ventana_sem_max')
        fin=ini+int(vm)-1 if vm else ini
    try: ws=int(r[7])
    except: ws=None
    y2025 = r[6].startswith('2025')
    # si la siembra fue en 2025 y el inicio de cosecha NO se devolvio al arranque del ano,
    # esa cosecha ocurrio en 2025 y no cuenta para las semanas 22-33 de 2026
    if y2025 and ws is not None and ini>=ws: continue
    lot.append((g,dig(r[5] or r[4]),ini,max(fin,ini)))

den=collections.defaultdict(int)   # (grupo,semana) -> plantas
for g,pl,ini,fin in lot:
    for w in range(ini,fin+1):
        if 22<=w<=33: den[(g,w)]+=pl

# ---------- numerador: tallos reales ----------
num=collections.defaultdict(int)
dias=collections.defaultdict(set)
for x in csv.DictReader(open(P+'registro_tallos.csv')):
    f=x['Fecha']
    if not f or not f[0].isdigit(): continue
    d=datetime.date.fromisoformat(f); w=d.isocalendar()[1]
    if not (22<=w<=33): continue
    g=REG.get(x['Grupo'].strip())
    if not g: continue
    t=dig(x['Tallos frescos'])+dig(x['Tallos secos'])
    num[(g,w)]+=t
    if t: dias[w].add(d)

# ---------- factor observado ----------
res={}
print('%-22s %9s %12s %10s %10s %8s'%('GRUPO','tallos','plantas-sem','OBSERVADO','TEORICO','ratio'))
for g in sorted({k[0] for k in num}):
    T=sum(v for k,v in num.items() if k[0]==g)
    D=sum(v for k,v in den.items() if k[0]==g)
    nw=len({k[1] for k in num if k[0]==g and num[k]>0})
    c=C.get(g,{})
    teo=None
    if c.get('tallos_planta') not in (None,'','SIN_DATO') and c.get('ventana_sem_max'):
        teo=float(c['tallos_planta'])/float(c['ventana_sem_max'])
    if D>0:
        obs=T/D
        res[g]=dict(obs=obs,tallos=T,plantasem=D,semanas=nw,teorico=teo)
        print('%-22s %9d %12d %10.4f %10s %8s'%(g,T,D,obs,'%.4f'%teo if teo else 'SIN_DATO',
              '%.2fx'%(obs/teo) if teo else '-'))
    else:
        print('%-22s %9d %12d %10s   (sin lotes cruzados)'%(g,T,D,'-'))
json.dump(res,open('factores.json','w'))
print()
print('dias de cosecha por semana:', {w:len(dias[w]) for w in sorted(dias)})
