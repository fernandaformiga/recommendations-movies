ratings = {'Samuel': 
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
		 
from math import sqrt

def euclidian(user1, user2):
	si = {}
	for item in ratings[user1]: #validate common movies
		if item in ratings[user2]:
			si[item] = 1
	
	if len(si) == 0: #no movies in common
		return 0

	soma = sum([pow(ratings[user1][item] - ratings[user2][item],2)
			for item in ratings[user1] if item in ratings[user2]])

	return 1/(1 + sqrt(soma))


def get_similars(user):
	similarity = [(euclidian(user, other_user), other_user)
				for other_user in ratings if other_user != user]
	similarity.sort()
	similarity.reverse()
	return similarity

#recommendations will be based on unwatched movies
#first, we get the similarity between our user and the others
#then we get rating * similarity = total
#then total/similarity sum for a movie

def get_recommendations(user):
	totals = {}
	sum_similarity = {}
	for other in ratings:
		if other == user: continue
		#continue won't run code below if both are the same
		similarity = euclidian(user, other)

		if similarity <= 0: continue
		
		for item in ratings[other]:
			if item not in ratings[user]:
				totals.setdefault(item,0)
				totals[item] += ratings[other][item] * similarity
				sum_similarity.setdefault(item,0)
				sum_similarity[item] += similarity
	rankings = [(total/sum_similarity[item], item) for item, total in totals.items()]
	rankings.sort()
	rankings.reverse()
	return rankings

print(get_recommendations('Johnny'))

#it is possible to invert the database and get similar movies rather than similar user tastes