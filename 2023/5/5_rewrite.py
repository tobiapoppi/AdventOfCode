with open('2023/5/input.txt', 'r') as f:
    lines = f.read().split('\n')

def get_mappings_and_seeds(lines):
    mappings = {}
    seeds = []
    current_mapping = None
    for line in lines:
        if line:
            if line.startswith('seeds:'):
                seeds = [int(x) for x in line[7:].split()]
            elif line[0].isalpha():
                current_mapping = line.split()[0]
                mappings[current_mapping] = []
            else:
                dr, sr, l = [int(x) for x in line.split()]
                mappings[current_mapping].append((sr, sr + l - 1, dr - sr))
    return seeds, mappings

def cut_ranges(seed_range, map_range):
    seed_start = seed_range[0]        
    seed_end = seed_range[1]        
    map_start = map_range[0]        
    map_end = map_range[1]
    if seed_start < map_start and seed_end > map_end:
        return [(map_start,map_end)], [(seed_start, map_start-1), (map_end+1, seed_end)]
    elif seed_start < map_start <= seed_end:
        return [(map_start, seed_end)], [(seed_start, map_start-1)]
    elif seed_start <= map_end < seed_end:
        return [(seed_start, map_end)], [(map_end+1, seed_end)]
    elif seed_start >= map_start and seed_end <= map_end:
        return [(seed_start,seed_end)], []
    else:
        return [], [(seed_start, seed_end)]

def process_seeds(seeds, mappings):
    ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    for map in mappings.values():
        new_map_ranges = []
        for seed_range in ranges:
            not_processed = [seed_range]
            for map_range in map:
                new_unconvenient_ranges = []
                for part_range in not_processed:
                    mod_range, other_ranges = cut_ranges(part_range, map_range)
                    new_unconvenient_ranges.extend(other_ranges)
                    new_map_ranges.extend([(s + map_range[2], e + map_range[2]) for s, e in mod_range])
                not_processed = new_unconvenient_ranges
            new_map_ranges.extend(not_processed)
        ranges = new_map_ranges
    return ranges

seeds, mappings = get_mappings_and_seeds(lines)
final_ranges = process_seeds(seeds, mappings)
min_location = min(r[0] for r in final_ranges)
print(min_location)
