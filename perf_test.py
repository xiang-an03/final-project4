import time
from api import main as mod

artists = mod.get_global_celebrities_by_gender_cached('male')
print('artists_count:', len(artists))

start_all = time.time()
for a in artists[:6]:
    t0 = time.time()
    res = mod.process_single_artist(a, ['dog_style','singer'])
    elapsed = time.time() - t0
    print(f"{a}: {elapsed:.3f}s -> {'found' if res else 'none'}")
print('total:', time.time() - start_all)
