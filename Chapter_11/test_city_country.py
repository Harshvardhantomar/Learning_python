from city_country_population import about_city as pop
from city_country import about_city

def test_city_country():
    ans = pop('gwalior','india')
    assert ans == 'Gwalior, India'
    
def test_city_country_population():
    ans = pop('gwalior','india',50000)
    assert ans == 'Gwalior, India - Population 50000'
    
