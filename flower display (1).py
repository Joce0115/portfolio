# jocelyn garcia
#02/21/2025
#vacation

#int
import random
flower = ["https://tinyurl.com/4f7ba4ks",
          "https://cdn.mos.cms.futurecdn.net/CDjnTYxBJ3xgDSEprNt4CR-1024-80.jpg.webp",
          "https://www.herbaldynamicsbeauty.com/cdn/shop/articles/roses-skin-benefits_1400x.progressive.jpg?v=1617126403",
          "https://i.guim.co.uk/img/media/31108a88f4783bee63ab6cd1a37f6cd6f9c699ff/0_0_5000_3000/master/5000.jpg?width=620&dpr=1&s=none&crop=none",
          "https://wpcdn.us-east-1.vip.tn-cloud.net/www.hawaiimagazine.com/content/uploads/2023/05/i/i/thumbnail-rect-supernova-3x4-1-1024x768.jpeg"
          ]
from PIL import Image
import requests
from io import BytesIO


#intro
def open_image(url):
    response = requests.get(url) # HTTP request
    img = Image.open(BytesIO(response.content)) # makes image an opject
    img.show() # shows the image


def flower_idea():
    print("Welcome to flower recommender")
    while True:
    #ask for an input
        ans=input("would you like a recommendation? Enter: ")
        if ans == "Yes" or ans == "yes" or ans == "y" or ans=="ye" or ans=="yeah":
            #Generate a randome image from out list
                flowerType= random.randint(0,4)

                if flowerType == 0: #habiscus
                        open_image(flower[0])
                        print("I recommend a hibiscus flower because it represents transient beauty and the importance of living in the moment.") # description of the dog in this position

                elif flowerType == 1: #greece
                        open_image(flower[1])
                        print("i reccomment dahlia because it symbolizes dignity, eternal love, and commitmen." )

                elif flowerType == 2: #greece
                        open_image(flower[2])
                        print("i reccomment roses because it symbolizes love, royalty, beauty, sensuality, secrecy, and mysticism." )

                elif flowerType == 3: #greece
                        open_image(flower[3])
                        print("i reccomment tulip because it symbolizes perfect and deep love.")

                elif flowerType == 4: #greece
                        open_image(flower[4])
                        print("i reccomment plumeria because it symbolizes  a new beginning, beauty, charm, and grace, spring, new life, new beginning, or birth.")

        elif ans == "No" or ans == "n" or ans == "no":
                print("Good bye. Have a good day")
                break


flower_idea()

#1 hibiscus : https://salife.com.au/gardens/grow-your-own-hibiscus/ #title: Grow your own Hibiscus, Author: Jason Scroop, published, apri 19,2024
#2 dahlia : https://www.gardeningknowhow.com/ornamental/bulbs/dahlia/different-varieties-of-dahlia.htm title: Dahlia Plant Types: What Are The Different Varietis Of Dahlia author: leonkenig published: 2022
#3 rose :https://www.herbaldynamicsbeauty.com/blogs/herbal-dynamics-beauty/the-many-benefits-of-roses-for-skin  title:The Beautiful Benefits of Roses for Skin published:june 07,2023 Author:unkown
#4 Tulip: https://www.theguardian.com/lifeandstyle/2023/mar/31/tulips-are-a-must-for-spring-but-sustainable-ones-are-far-more-classy title: Tulips are a must for spring - but go sustainable to keep it classy author: Mikhail Abramov/Getty Images published: Fri 31 Mar 2023 publised: Alice Vincent
#5 plumeria: https://www.hawaiimagazine.com/see-some-of-the-rarest-plumeria-in-the-world-on-this-north-shore-farm-tour/ Photo: Courtesy of Little Plumeria Farm/Rich Tully title: See Some of the Rarest Plumeria in the World on this North Shore Farm Tour published:May 8, 2023 publisher:Kevin Allen
