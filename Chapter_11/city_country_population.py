def about_city(city,country,population=''):
    if population:
        ans = f'{city}, {country} - population {population}'
    else:
        ans = f'{city}, {country}'
    return ans.title()