#movie-based approach

user_ratings = {'Samuel': 
		{'Lord of the Rings trilogy': 5.0,
		 'Parasite': 4.5, 
		 'Forrest Gump': 4.5,
		 'Bacurau': 3.5},
	 
	  'Alice': 
		{'Lord of the Rings trilogy': 4.5, 
		 'Forrest Gump': 4.5, 
		 'A Clockwork Orange': 2.5},
	 
	  'Vitor': 
		{'Lord of the Rings trilogy': 4.5,
		 'Forrest Gump': 1.5, 
		 'A Clockwork Orange': 4.5},
			 
	  'Pedro': 
		{'Lord of the Rings trilogy': 4.5, 
		 'Amadeus': 4.0,
		 'Parasite': 5.0, 
		 'Forrest Gump': 5.0, 
		 'A Clockwork Orange': 5.0, 
		 'Bacurau': 4.0},
				 
	  'Johnny': 
		{'Lord of the Rings trilogy': 5.0, 
		 'Amadeus': 3.5,
		 'Parasite': 4.0, 
		 'Forrest Gump': 4.5, 
		 'Bacurau': 4.0},

	  'Natalia': 
		{'Lord of the Rings trilogy': 5.0, 
		 'Forrest Gump': 4.0, 
		 'A Clockwork Orange': 3.5, 
		 'Bacurau': 4.0},
			  
	  'Seiki': 
		{'Lord of the Rings trilogy': 4.0},

	  'Fischer':
		{'Lord of the Rings trilogy': 4.5, 
		 'Amadeus': 3.5,
		 'Forrest Gump': 5.0, 
		 'A Clockwork Orange': 2.0, 
		 'Bacurau': 5.0}}

movie_ratings = {'Lord of the Rings trilogy':
            {'Samuel': 5.0,
            'Alice': 4.5,
            'Vitor': 4.5,
            'Pedro': 4.5,
            'Johnny': 5.0,
            'Natalia': 5.0,
            'Seiki': 4.0,
            'Fischer': 4.5},

            'Amadeus':
            {'Pedro': 4.0,
            'Johnny': 3.5,
            'Fischer': 3.5},

            'Parasite':
            {'Samuel': 4.5,
            'Pedro': 5.0,
            'Johnny': 4.0},

            'A Clockwork Orange':
            {'Alice': 2.5,
            'Vitor': 4.5,
            'Pedro': 5.0,
            'Johnny': 4.5,
            'Natalia': 3.5,
            'Fischer': 2.0},

            'Forrest Gump':
            {'Samuel': 4.5,
            'Alice': 4.5,
            'Vitor': 1.5,
            'Pedro':5.0,
            'Johnny': 4.5,
            'Natalia': 4.0,
            'Fischer': 5.0},

            'Bacurau':
            {'Samuel': 3.5,
            'Pedro': 4.0,
            'Johnny': 4.0,
            'Natalia': 4.0,
            'Fischer': 5.0}}


from math import sqrt

def euclidian(base, user1, user2):
	si = {}
	for item in base[user1]: #validate common movies
		if item in base[user2]:
			si[item] = 1
	
	if len(si) == 0: #no movies in common
		return 0

	soma = sum([pow(base[user1][item] - base[user2][item],2)
			for item in base[user1] if item in base[user2]])

	return 1/(1 + sqrt(soma))


def get_similars(base, user):
	similarity = [(euclidian(base, user, other_user), other_user)
				for other_user in base if other_user != user]
	similarity.sort()
	similarity.reverse()
	return similarity

def get_recommendations_user(base, user):
	totals = {}
	sum_similarity = {}
	for other in base:
		if other == user: continue
		#continue won't run code below if both are the same
		similarity = euclidian(base, user, other)

		if similarity <= 0: continue
		
		for item in base[other]:
			if item not in base[user]:
				totals.setdefault(item,0)
				totals[item] += base[other][item] * similarity
				sum_similarity.setdefault(item,0)
				sum_similarity[item] += similarity
	rankings = [(total/sum_similarity[item], item) for item, total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

def calc_similar_items(base):
    result = {}
    for item in base:
        ratings = get_similars(base, item)
        result[item] = ratings
    return result

#similar_items = calc_similar_items(movie_ratings)
#print(similar_items)

def get_rec_items(baseUser, sim_items, user):
    ratingsUser = baseUser[user]
    ratings = {}
    total_similarity = {}
    for (item, rating) in ratingsUser.items():
        for (similarity, item2) in sim_items[item]:
            if item2 in ratingsUser: continue
            ratings.setdefault(item2, 0)
            ratings[item2] += similarity * rating
            total_similarity.setdefault(item2, 0)
            total_similarity[item2] += similarity
        rankings = [(score/total_similarity[item], item) for item, score in ratings.items()]
        rankings.sort()
        rankings.reverse()
        return rankings

#listItems = calc_similar_items(movie_ratings)
#print(get_rec_items(user_ratings, listItems, 'Samuel'))