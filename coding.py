"""Given list of dicts..."""

book_list = [
    {'title': 'The Escapist', 'author': "Sam Clay", 'publisher': 'Empire Comics','publication_date': 
        {
            'year': 1939,
            'month': 'October',
            'day': 15,
        },
    },
    {'title': 'The Ascapist', 'author': "Sam Alay", 'publisher': 'Ampire Comics','publication_date': 
            {
                'year': 1929,
                'month': 'September',
                'day': 15,
            },
    },
    {'title': 'The Oscapist', 'author': "Sam Olay", 'publisher': 'Ompire Comics','publication_date': 
        {
            'year': 1939,
            'month': 'October',
            'day': 15,
        }

    }
]

# Order by author
sorted(book_list, key=lambda k: k['author'])