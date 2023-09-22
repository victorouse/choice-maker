domains = [
    "victorouse.ai",
    "victorouse.blog",
    "victorouse.ceo",
    "victorouse.computer",
    "victorouse.dev",
    "victorouse.engineer",
    "victorouse.engineering",
    "victorouse.gg",
    "victorouse.io",
    "victorouse.is",
    "victorouse.phd",
    "victorouse.sh",
    "victorouse.software",
    "victorouse.tech",
    "victorouse.website",
    "victorouse.xyz",
    "victorouse.zip",
]


def interactive_sort(domains):
    sorted_domains = [domains[0]]

    for domain in domains[1:]:
        inserted = False
        for i, sorted_domain in enumerate(sorted_domains):
            preference = (
                input(f"{domain} 👈 OR 👉 {sorted_domain} (1 / 2): ").strip().lower()
            )
            if preference == "1":
                sorted_domains.insert(i, domain)
                inserted = True
                break
        if not inserted:
            sorted_domains.append(domain)

    print("\nTop 5 Preferred Domains:")
    for i in range(min(5, len(sorted_domains))):
        print(f"{i + 1}. {sorted_domains[i]}")

    return sorted_domains


sorted_domains = interactive_sort(domains)
