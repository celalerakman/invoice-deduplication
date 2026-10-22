"""Find duplicate supplier invoices without conflating different suppliers."""
from collections import defaultdict
import re


def duplicates(rows):
    grouped = defaultdict(list)
    for index, row in enumerate(rows, start=1):
        supplier = row['supplier'].strip().casefold()
        invoice = re.sub(r'\s+', '', row['invoice']).casefold()
        if not supplier or not invoice:
            raise ValueError('Supplier and invoice required')
        grouped[(supplier, invoice)].append(index)
    return {key: indexes for key, indexes in grouped.items() if len(indexes) > 1}


if __name__ == '__main__':
    print(duplicates([{'supplier':'ACME','invoice':'INV 17'},
                      {'supplier':'acme','invoice':'inv17'}]))
