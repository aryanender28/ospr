def optimal_page_replacement(pages, capacity):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < capacity:
                memory.append(pages[i])
            else:
                future_uses = []
                for page in memory:
                    if page in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(page))
                    else:
                        future_uses.append(float('inf'))
                page_to_replace = future_uses.index(max(future_uses))
                memory[page_to_replace] = pages[i]
            page_faults += 1
        print(f"Step {i+1}: Page {pages[i]} -> Memory: {memory}")
    print(f"\nTotal Page Faults: {page_faults}")

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 3
optimal_page_replacement(pages, capacity)
