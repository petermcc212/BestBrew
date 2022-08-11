import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestbrew.settings')

import django
django.setup()
from rango.models import CoffeeType, UserProfile, CoffeeShop, CoffeeShopType, Blog, Visited, VisitedCoffeeShop, AdminBlog
from django.contrib.auth.models import User
from datetime import datetime


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    coffee_types = [
        {"type": "Latte",
         "description": "A latte is a coffee drink made with espresso and steamed milk.",
         "image": "coffee_types/Latte.jpg",
         "slug": "Latte"},
        {"type": "Cappuccino",
         "description": "A cappuccino is an espresso-based coffee drink that originated in Italy, and is traditionally prepared with steamed milk foam.",
         "image": "coffee_types/Cappuccino.jpg",
         "slug": "Cappuccino"},
        {"type": "Espresso",
         "description": "Espresso is coffee of Italian origin, brewed by expressing or forcing a small amount of nearly boiling water under pressure through finely ground coffee beans..",
         "image": "coffee_types/Espresso.jpg",
         "slug": "Espresso"},
        {"type": "Long black",
         "description": "A long black is a style of coffee commonly found in New Zealand and Australia..",
         "image": "coffee_types/Long black.jpg",
         "slug": "Long black"},
        ]

    coffee_shops = [
        {"name": "Artisan Roast",
         "address": "15-17 Gibson St, Glasgow.",
         "phone": "07864 984253",
         "postcode": "G12 8NU",
         "email": "test@abc.com",
         "latitude": "55.872288",
         "longtitude": "-4.282119",
         "image": "coffee_shop/ArtisanRoast.jpg",
         "slug": "ArtisanRoast"},
        {"name": "Starbucks Coffee",
         "address": "9 Exchange Pl, Glasgow ",
         "phone": "0141 204 2767",
         "postcode": "G1 3AN",
         "email": "starbucks@abc.com",
         "latitude": "55.861911",
         "longtitude": "-4.254723",
         "image": "coffee_shop/Startbucks.jpg",
         "slug": "Starbucks Coffee"},
        {"name": "Tinderbox",
         "address": "18 Ingram St, Glasgow ",
         "phone": "0141 552 6907",
         "postcode": "G1 1EJ",
         "email": "Tinderbox@abc.com",
         "latitude": "55.859669",
         "longtitude": "-4.24616",
         "image": "coffee_shop/Tinderbox.jpg",
         "slug": "Tinderbox"},
        {"name": "The Balcony Cafe",
         "address": "534 Paisley Rd West, Glasgow .",
         "phone": "0141 427 9550",
         "postcode": "G51 1RN",
         "email": "balcony@abc.com",
         "latitude": "55.850744",
         "longtitude": "-4.304923",
         "image": "coffee_shop/BalconyCafe.jpg",
         "slug": "The Balcony Cafe"},
    ]

    blogs = [
        {"type": "shop",
         "content": "Very good shop.",
         "date": "2019-03-03 17:51:28",
         "rating": 4,
         "latitude": "55.859669",
         "longtitude": "-4.24616"},
        {"type": "shop",
         "content": "I like this shop a lot.",
         "date": "2019-03-08 12:51:28",
         "rating": 5,
         "latitude": "55.872288",
         "longtitude": "-4.282119"},
        {"type": "shop",
         "content": "Not bad for coffee.",
         "date": "2019-03-12 10:41:28",
         "rating": 4,
         "latitude": "55.874288",
         "longtitude": "-4.272119"},
        {"type": "shop",
         "content": "I dont like this shop.",
         "date": "2019-03-15 12:51:28",
         "rating": 1,
         "latitude": "55.8642705",
         "longtitude": "-4.2976255"},
    ]

    admin_blogs = [
        {"title": "CoffeeShop 'Waverly' Fine Art Texture Set!",
         "subtitle": "The first entry",
         "blogbody": "Well, I am back! Our family caught a lovely stomach bug and have been down for much of the last 5 days. So I haven't had the energy to get on my computer much."
                       +"\n Today I am feel much better and so I designed this new fine art fabric texture pack. It comes with 7 beautiful textures, and you can even desaturate one if you don't want to change the color on your image. I love using these in Soft Light, Overlay, Multiple, or Screen blending modes on my images.",
         "image": "blog/jo-lanta-654165-unsplash.jpg",
         "date": "2019-03-13 16:11:39",
         "author": "anonymous"},
        {"title": "In Kansas City, Pushing The Culture Forward At Monarch Coffee",
         "subtitle": "Second post.",
         "blogbody": "Stepping into Monarch Coffee in Kansas City feels like you’ve suddenly been transported eight hours forward in time and roughly 4,500 miles east. The Parisian aesthetics (reinforced through Instagram imagery) and detailed botanical wallpaper beckon even the shyest of selfiers to snap away in a fit of self-documentation. The space is simultaneously clean, intelligent, calming, and indisputably cute. But beyond the beautiful design, there is a holistic intentionality at work here, built around bringing people of all walks of life together in a comfortable, forward-thinking space."
                        + "\n The brainchild of Tyler and Jaime Rovenstine, Monarch Coffee’s mission becomes clearer when given some context. Tyler, a long and pedigreed member of the Kansas City coffee community as well as regional Barista Champion (South Central, 2014), sought to instill the space with some of the practices he picked up along the competition circuit. “We wanted to give the level of attention that’s given to judges [in competition] to the customer,” he tells Sprudge. Water service extends to guests in every corner of the cafe, for example, and seasonal signature beverages are given a prominent menu presence.",
         "image": "blog/mike-kenneally-46284-unsplash.jpg",
         "date": "2019-03-13 16:17:31",
         "author": "Charlie Burt"},
        {"title": "Blanchard’s Coffee Branches Into The Cafe Space With Two Richmond Shops",
         "subtitle": "Third Post",
         "blogbody": "It can be hard out there for wholesale coffee roasters. As we gleaned from this year’s Build-Outs of Summer, it seems just about everyone roasts or wants to roast. And those adhering to the no-longer-en-vogue multi-roaster model are more inclined to stick with a few permanent options instead of rotating regularly. And even when they do find a home in a cafe, wholesale-only roasters’ entire consumer interaction is left outside their own hands."
                        + "\n The most obvious solution (if not also the most expensive) is to open a coffee shop of their own. And that’s exactly what Richmond, Virginia’s Blanchard’s Coffee Roasting Co is doing. After 14 years in existence, Blanchard’s is opening not one but two shops in as many years."
                        + "\n The expansion into the cafe space will be gradual for the company; the first location—in a “historic building in the 3100 block of West Broad Street, Richmond,” per a press release—is scheduled to be open some time in the summer of 2019. The second location, “part of a new mixed use development on Richmond’s Forest Hill Avenue,” is expected to fruition in spring of the following year. Blanchard’s will work with architectural design firm Fultz & Singh Architects on both locations."
                        + "\n For founder David Blanchard, these cafes are a long time coming. “We have thought about opening a cafe every year for the last 10 years. However, the momentum of our business has always pushed us to further our investment in roasting infrastructure,” Blanchard tells Sprudge. But it wasn’t until a family vacation at the end of 2018 that finally convinced him to put the wheels in motion."
                        + "\n “My wife, Kelly, two daughters, Molly and Ann-Cason, and I spent a week in San Francisco. One of our vacation traditions is to visit local cafes, and I witnessed a light click on in my children’s minds as we visited cafes in San Francisco and Santa Cruz. They have been around coffee their entire lives, but they saw coffee from a different point of view in on that trip,” Blanchard states. “As we were flying home, I thought about Molly and Ann-Cason’s coffee ‘enlightenment’ and thought about our farmer relationships. Blanchard’s brick and mortar cafes would give us a larger stage to tell coffee’s story from our perspective as roasters. Cafes would force us to double down on education, incorporating educational opportunities for both our wholesale partners and retail clients alike, creating a robust platform from which we can push sustainable coffee culture further in our community and beyond."
                        + "\n These cafes are just the start for Blanchard’s expansion plans. There are murmurs of other projects in the works beyond Richmond that have yet to be finalized. For now, they are doing the extremely difficult task of building two coffee shops at the same time. They are taking control of their narrative and expanding the platform upon which they can tell their stories and of those they work with. For more information, visit Blanchard’s Coffee Roasting Co’s official website."
                        + "\n Zac Cadwalader is the managing editor at Sprudge Media Network and a staff writer based in Dallas. Read more Zac Cadwalader on Sprudge.",
         "image": "blog/robert-shunev-526485-unsplash.jpg",
         "date": "2019-03-13 16:19:39",
         "author": "Zac Cadwalader"},
        {"title": "Are Visa Denials The New Normal At World Coffee Competitions?",
         "subtitle": "Fourth post.",
         "blogbody": "News broke last week (since confirmed by World Coffee Events) that 2018 Mexican Brewers Cup champion Carlos Maqueda had been denied a visa by the United States government, and will not be allowed entry into the country to compete at the World Barista Championship in Boston next month. As of the time of reporting, Sprudge can update that a total of four coffee competitors have been denied visas to attend the Boston event: both Maqueda and Emilio Arturo of Mexico, as well as the Barista and Brewers Cup champions from the United Arab Emirates Michaela Ruazol and Lablibell Bajarias, respectively."
                     + "\n Update 3/12/2019: Lablibell Bajarias was approved for a visa on Monday 3/11/19 and will be attending the 2019 World Brewers Cup in Boston."
                     + "\n As the adverse effects of international tensions trickle outside the bureaucratic world and into the lives of real, actual people, many in the coffee community are left with more questions than answers. Visa denials are constantly looming at World events; indeed, those international tensions can play out directly when it comes to accessing coffee’s grandest stage."
                     + "\n World Coffee Events brand manager (and former Sprudge editor) Alex Bernson told us that the exact number of visa denials over the near two decades of World Barista Championship events is difficult to know. While there are high profile cases of competitors having visa issues that play out publicly—perhaps none more famous that Iran’s first barista champion Mehran Mohammadnezhad Mirjani being denied and then finally approved for his visa at the 11th hour to compete in Seattle in 2015—many can go unnoticed. “We don’t always receive full or even any reports from competitors and national bodies as to why they aren’t attending or sending a second place competitor instead of a first,” Bernson tells Sprudge, “nor do we necessarily expect everyone to let us know when they’re having visa specific troubles, because there are many reasons both political and personal that may be the case."
                     + "\n According to Bernson, issues related to past visa denials are long-ranging, and oftentimes unexpectedly personal. “[It could be] everything from not filling out forms exactly correctly to an embassy’s satisfaction on a first or second try, to having a citizenship from a country in Central Asia but working in and representing a European national body,” Bernson tells Sprudge. “Sometimes the process takes too long and they don’t get their visas in time, especially with later championships. Sometimes competitors get a visa but their coaches and support people do not. Sometimes a person’s individual history in their own country or a host country may come into play with a government’s decision. Sometimes items are held in customs or huge costs and extremely intricate processes for visas are imposed on certain countries by other countries’ governments.”",
         "image": "blog/robert-shunev-526485-unsplash.jpg",
         "date": "2019-03-13 16:23:08",
         "author": "Zac Cadwalader"},
    ]

    user = User.objects.first()


    for coffeeType in coffee_types:
        add_coffee_type(coffeeType)

    for coffeeShop in coffee_shops:
        add_coffee_shop(coffeeShop)

    add_user_profile(user)

    visit = add_visited(user)

    coffee_shop_list = CoffeeShop.objects.all()
    for coffeeShop in coffee_shop_list:
        for blog in blogs:
            add_blog(blog, user, coffeeShop)
        add_visited_shop(visit, coffeeShop)

    for adminBlog in admin_blogs:
        add_admin_blog(adminBlog)




def add_visited(user):
    visit = Visited()
    visit.user = user
    visit.save()
    return visit

def add_visited_shop(visit, coffeeShop):
    visit_coffee_shop = VisitedCoffeeShop()
    visit_coffee_shop.visited = visit
    visit_coffee_shop.coffee_shop = coffeeShop
    visit_coffee_shop.date = datetime.now()
    visit_coffee_shop.save()



def add_coffee_shop(coffeeShopDict):
    coffeeShop = CoffeeShop()

    coffeeShop.name = coffeeShopDict['name']
    coffeeShop.address = coffeeShopDict['address']
    coffeeShop.phone = coffeeShopDict['phone']
    coffeeShop.postcode = coffeeShopDict['postcode']
    coffeeShop.email = coffeeShopDict['email']
    coffeeShop.latitude = coffeeShopDict['latitude']
    coffeeShop.longtitude = coffeeShopDict['longtitude']
    coffeeShop.image = coffeeShopDict['image']
    coffeeShop.slug = coffeeShopDict['slug']
    coffeeShop.save()

    coffeeTypes = CoffeeType.objects.all()

    coffeeShopType = CoffeeShopType()
    coffeeShopType.coffee_shop = coffeeShop
    coffeeShopType.coffee_type = coffeeTypes[0]
    coffeeShopType.save()

    coffeeShopType = CoffeeShopType()
    coffeeShopType.coffee_shop = coffeeShop
    coffeeShopType.coffee_type = coffeeTypes[1]
    coffeeShopType.save()
    return coffeeShop

def add_coffee_type(coffeeTypeDict):
    coffeeType = CoffeeType()

    coffeeType.type = coffeeTypeDict['type']
    coffeeType.description = coffeeTypeDict['description']
    coffeeType.image = coffeeTypeDict['image']
    coffeeType.slug = coffeeTypeDict['slug']
    coffeeType.save()
    return coffeeType

def add_user_profile(user):
    userProfile = UserProfile()
    userProfile.user = user
    userProfile.city = 'Glasgow'
    userProfile.website = 'http://www.test.co.uk'
    userProfile.phone = '565656'
    userProfile.image = 'profile_image/profile.jpg'
    userProfile.save()

def add_blog(blogDict, user, coffeeShop):
    blog = Blog()

    blog.type = blogDict['type']
    blog.content = blogDict['content']
    blog.date = datetime.strptime(blogDict['date'],'%Y-%m-%d %H:%M:%S')
    blog.rating = blogDict['rating']
    blog.latitude = blogDict['latitude']
    blog.longtitude = blogDict['longtitude']
    blog.user = user
    blog.coffee_shop = coffeeShop

    blog.save()

def add_admin_blog(blogDict):
    adminBlog = AdminBlog()

    adminBlog.title = blogDict['title']
    adminBlog.subtitle = blogDict['subtitle']
    adminBlog.blogbody = blogDict['blogbody']
    adminBlog.image = blogDict['image']
    adminBlog.date = datetime.strptime(blogDict['date'],'%Y-%m-%d %H:%M:%S')
    adminBlog.author = blogDict['author']
    adminBlog.save()


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()