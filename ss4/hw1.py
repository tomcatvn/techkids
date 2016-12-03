def display_movie(m):
    print("Original name", m["o_name"])
    print("Translated name",m["t_name"])
    print("Year",m["year"])
    print()
def create_movie(o_name,t_name,year):
    return {
        "o_name" : o_name,
        "t_name" : t_name,
        "year" : year
        }
movie0 = create_movie("the hunger games","dau truong sinh tu",2016)
display_movie(movie0)

def display_movie_list(m_list):
    for i in m_list:
        display_movie(i)
    print("------------------------")
    print()

movie_list= []
movie1 = create_movie("little door gods","tieu mon thien",2015)
movie_list.append(movie0)
movie_list.append(movie1)

display_movie_list(movie_list)

def remove_movie(m_list,movie):
    m_list.pop(m_list.index(movie))

movie_list = [movie0,movie1]
remove_movie(movie_list,movie0)
display_movie_list(movie_list)

def search_movie_by_year(m_list,year):
    search_movie = []
    for i in m_list:
        if i["year"] == year:
            search_movie.append(i)
    return search_movie
            
    

movie_list.append(create_movie("break point","ranh gioi chet",2015))
movie_in_2015 = search_movie_by_year(movie_list,2015)
display_movie_list(movie_in_2015)
