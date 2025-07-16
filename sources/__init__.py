# Ensures that a generator never returns the same item twice
# 
# Accepts:
# - A generator
# Returns:
# - A generator containing the same items, but never repeating
def no_repeats(generator):
    seen = set()
    for obj in generator:
        if not obj in seen:
            seen |= {obj}
            yield obj

# Combine generators into a single generator, in a round-robin fashion
# 
# Accepts:
# - sources: a list of generators
# Returns:
# - A generator which retreives items from provided generators in a round-robin fashion
def round_robin(generators):
    # Continue iterating until all sources are depleted
    while len(generators) > 0:
        # Iterate through sources in reverse to allow removal of sources when depleted
        for generator in generators[:]:
            # Attempt to get the next article in the source
            try:
                yield next(generator)
            # If the source is depleted, remove it
            except StopIteration:
                generators.remove(generator)
