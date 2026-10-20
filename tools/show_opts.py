import sys,glob
sys.path.insert(0,'practice')
from build_practice import parse
key=sys.argv[1]
for p in sorted(glob.glob(f'practice/src/{key}-p*.txt')):
    for q in parse(p):
        if q['typ']!='MC': continue
        L=[len(o) for o in q['opts']]
        if L.index(max(L))!=ord(q['ans'][0])-65: continue
        print(f"Q{q['n']} ans={q['ans'][0]} lens={L}")
        for o in q['opts']: print('  '+o)
