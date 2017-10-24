import random as random
from datetime import datetime
# pull creds
from settings import mongo_url
# import driver
import pymongo
# import client function
from pymongo import MongoClient
# create client
client = pymongo.MongoClient(mongo_url, ssl=True)
# imort UUID functionality
import uuid

if client:
    print("client working.")
# define database
db = client.test_database
# define collections
collection = db.test_collection
users = db.user_collection
dogs = db.dogs_collection
breeds = db.breeds_colletion

dog_names = [
    "Jason",
    "Lucy",
    "Daisy"
    "Paul",
    "Monis",
    "Molly",
    "Lora",
    "Justin",
    "Bailey",
    "Maggie",
    "Chloe",
    "Lily",
    "Stella",
    "Zoey",
    "Penny",
    "Roxy",
    "Coco",
    "Gracie",
    "Ruby",
    "Mia",
    "Zoe",
    "Greg",
    "Nala",
    "Rosie",
    "Ginger",
    "Abby",
    "Josh",
    "Piper",
    "Sasha",
    "Riley",
    "Pepper",
    "Lulu",
    "Emma",
    "Lady",
    "Layla",
    "Lexi",
    "Olive",
    "Annie",
    "Izzy",
    "Maya",
    "Maddie",
    "Dixie",
    "Princess",
    "Cali",
    "Millie",
    "Belle",
    "Ella",
    "Harley",
    "Honey",
    "Kona",
    "Charlie",
    "Manny",
    "Marley",
    "Roxie",
    "Cookie",
    "Scout",
    "Holly",
    "Minnie",
    "Winnie",
    "Angel",
    "Dakota",
    "Callie",
    "Missy",
    "Phoebe",
    "Hazel",
    "Athena",
    "Shelby",
    "Peanut",
    "Sugar",
    "Jasmine",
    "Ava",
    "Penelope",
    "Sandy",
    "Ahmer",
    "Gigi",
    "Fiona",
    "Chance",
    "Josie",
    "Cleo",
    "Mocha",
    "Leia",
    "Delilah",
    "Baby",
    "Harper",
    "Shadow",
    "Macy",
    "Pearl",
    "Allie",
    "Mila",
    "Heidi",
    "Bonnie",
    "Nina",
    "Grace",
    "Katie",
    "Lacey",
    "Gypsy",
    "Cocoa",
    "Nova",
    "Charlotte",
    "Puppers"
]

dog_breeds = [
  "Affenpinscher",
  "Mixed",
  "Afghan Hound",
  "Afghan Shepherd",
  "Aidi",
  "Airedale Terrier",
  "Akbash",
  "Akita",
  "Alano Español",
  "Alaskan Husky",
  "Alaskan Klee Kai",
  "Alaskan Malamute",
  "Alaunt",
  "Alpine Dachsbracke",
  "Alpine Spaniel",
  "American Akita",
  "American Bulldog",
  "American Cocker Spaniel",
  "American English Coonhound",
  "American Eskimo Dog",
  "American Foxhound",
  "American Hairless Terrier",
  "American Pit Bull Terrier",
  "American Staffordshire Terrier",
  "American Water Spaniel",
  "Anatolian Shepherd Dog",
  "Andalusian Hound",
  "Anglo-Français de Petite Vénerie",
  "Appenzeller Sennenhund",
  "Ariege Pointer",
  "Ariegeois",
  "Armant",
  "Armenian Gampr dog",
  "Artois Hound",
  "Australian Cattle Dog",
  "Australian Kelpie",
  "Australian Shepherd",
  "Australian Silky Terrier",
  "Australian Stumpy Tail Cattle Dog[10]",
  "Australian Terrier",
  "Austrian Black and Tan Hound",
  "Austrian Pinscher",
  "Azawakh",
  "Bakharwal Dog",
  "Barbet",
  "Basenji",
  "Basque Ratter",
  "Basque Shepherd Dog",
  "Basset Artésien Normand",
  "Basset Bleu de Gascogne",
  "Basset Fauve de Bretagne",
  "Basset Griffon Vendéen, Grand",
  "Basset Griffon Vendéen, Petit",
  "Basset Hound",
  "Bavarian Mountain Hound",
  "Beagle",
  "Beagle-Harrier",
  "Bearded Collie",
  "Beauceron",
  "Bedlington Terrier",
  "Belgian Shepherd Dog (Groenendael)",
  "Belgian Shepherd Dog (Laekenois)",
  "Belgian Shepherd Dog (Malinois)",
  "Belgian Shepherd Dog (Tervuren)",
  "Bergamasco Shepherd",
  "Berger Blanc Suisse",
  "Berger Picard",
  "Bernese Mountain Dog",
  "Bichon Frisé",
  "Billy",
  "Black and Tan Coonhound",
  "Black and Tan Virginia Foxhound",
  "Black Norwegian Elkhound",
  "Black Russian Terrier",
  "Black Mouth Cur",
  "Bleu de Gascogne, Grand",
  "Bleu de Gascogne, Petit",
  "Bloodhound",
  "Blue Heeler",
  "Blue Lacy",
  "Blue Paul Terrier",
  "Blue Picardy Spaniel",
  "Bluetick Coonhound",
  "Boerboel",
  "Bohemian Shepherd",
  "Bolognese",
  "Border Collie",
  "Border Terrier",
  "Borzoi",
  "Bosnian Coarse-haired Hound",
  "Boston Terrier",
  "Bouvier des Ardennes",
  "Bouvier des Flandres",
  "Boxer",
  "Boykin Spaniel",
  "Bracco Italiano",
  "Braque d'Auvergne",
  "Braque du Bourbonnais",
  "Braque du Puy",
  "Braque Francais",
  "Braque Saint-Germain",
  "Brazilian Dogo",
  "Brazilian Terrier",
  "Briard",
  "Briquet Griffon Vendéen",
  "Brittany",
  "Broholmer",
  "Bruno Jura Hound",
  "Bucovina Shepherd Dog",
  "Bull and Terrier",
  "Bull Terrier",
  "Bull Terrier (Miniature)",
  "Bulldog",
  "Bullenbeisser",
  "Bullmastiff",
  "Bully Kutta",
  "Burgos Pointer",
  "Cairn Terrier",
  "Canaan Dog",
  "Canadian Eskimo Dog",
  "Cane Corso",
  "Cantabrian Water Dog",
  "Cão da Serra de Aires",
  "Cão de Castro Laboreiro",
  "Cão de Gado Transmontano",
  "Cão Fila de São Miguel",
  "Carolina Dog",
  "Carpathian Shepherd Dog",
  "Catahoula Leopard Dog",
  "Catalan Sheepdog",
  "Caucasian Shepherd Dog",
  "Cavalier King Charles Spaniel",
  "Central Asian Shepherd Dog",
  "Cesky Fousek",
  "Cesky Terrier",
  "Chesapeake Bay Retriever",
  "Chien Français Blanc et Noir",
  "Chien Français Blanc et Orange",
  "Chien Français Tricolore",
  "Chien-gris",
  "Chihuahua",
  "Chilean Fox Terrier",
  "Chinese Chongqing Dog",
  "Chinese Crested Dog",
  "Chinese Imperial Dog",
  "Chinook",
  "Chippiparai",
  "Chow Chow",
  "Cierny Sery",
  "Cirneco dell'Etna",
  "Clumber Spaniel",
  "Collie, Rough",
  "Collie, Smooth",
  "Combai",
  "Cordoba Fighting Dog",
  "Coton de Tulear",
  "Cretan Hound",
  "Croatian Sheepdog",
  "Cumberland Sheepdog",
  "Curly-Coated Retriever",
  "Cursinu",
  "Czechoslovakian Wolfdog",
  "Dachshund",
  "Dalmatian",
  "Dandie Dinmont Terrier",
  "Danish-Swedish Farmdog",
  "Deutsche Bracke",
  "Doberman Pinscher",
  "Dogo Argentino",
  "Dogo Cubano",
  "Dogue de Bordeaux",
  "Drentse Patrijshond",
  "Drever",
  "Dunker",
  "Dutch Shepherd",
  "Dutch Smoushond",
  "East Siberian Laika",
  "East European Shepherd",
  "Elo",
  "English Cocker Spaniel",
  "English Foxhound",
  "English Mastiff",
  "English Setter",
  "English Shepherd",
  "English Springer Spaniel",
  "English Toy Terrier (Black & Tan)",
  "English Water Spaniel",
  "English White Terrier",
  "Entlebucher Mountain Dog",
  "Estonian Hound",
  "Estrela Mountain Dog",
  "Eurasier",
  "Eurohound",
  "Field Spaniel",
  "Fila Brasileiro",
  "Finnish Hound",
  "Finnish Lapphund",
  "Finnish Spitz",
  "Flat-Coated Retriever",
  "Fox Terrier (Smooth)",
  "Fox Terrier, Wire",
  "French Brittany",
  "French Bulldog",
  "French Spaniel",
  "Gaddi Dog",
  "Galgo Español",
  "Galician Cattle Dog",
  "Garafian Shepherd",
  "Gascon Saintongeois",
  "Georgian Shepherd Dog",
  "German Longhaired Pointer",
  "German Pinscher",
  "German Roughhaired Pointer",
  "German Shepherd Dog",
  "German Shorthaired Pointer",
  "German Spaniel",
  "German Spitz",
  "German Wirehaired Pointer",
  "Giant Schnauzer",
  "Glen of Imaal Terrier",
  "Golden Retriever",
  "Gordon Setter",
  "Gran Mastín de Borínquen",
  "Grand Anglo-Français Blanc et Noir",
  "Grand Anglo-Français Blanc et Orange",
  "Grand Anglo-Français Tricolore",
  "Grand Griffon Vendéen",
  "Great Dane",
  "Great Pyrenees",
  "Greater Swiss Mountain Dog",
  "Greek Harehound",
  "Greenland Dog",
  "Greyhound",
  "Griffon Bleu de Gascogne",
  "Griffon Bruxellois",
  "Griffon Fauve de Bretagne",
  "Griffon Nivernais",
  "Guatemalan Dogo",
  "Hamiltonstövare",
  "Hanover Hound",
  "Hare Indian Dog",
  "Harrier",
  "Havanese",
  "Hawaiian Poi Dog",
  "Himalayan Sheepdog",
  "Hokkaido",
  "Hortaya Borzaya",
  "Hovawart",
  "Huntaway",
  "Hygenhund",
  "Ibizan Hound",
  "Icelandic Sheepdog",
  "Indian Pariah Dog",
  "Indian Spitz",
  "Irish Red and White Setter",
  "Irish Setter",
  "Irish Terrier",
  "Irish Water Spaniel",
  "Irish Wolfhound",
  "Istrian Coarse-haired Hound",
  "Istrian Shorthaired Hound",
  "Italian Greyhound",
  "Jack Russell Terrier",
  "Jagdterrier",
  "Jämthund",
  "Japanese Chin",
  "Japanese Spitz",
  "Japanese Terrier",
  "Kaikadi",
  "Kai Ken",
  "Kangal Dog",
  "Kanni",
  "Karakachan Dog",
  "Karelian Bear Dog",
  "Karst Shepherd",
  "Keeshond",
  "Kerry Beagle",
  "Kerry Blue Terrier",
  "King Charles Spaniel",
  "King Shepherd",
  "Kintamani",
  "Kishu Ken",
  "Komondor",
  "Kooikerhondje",
  "Koolie",
  "Korean Jindo",
  "Kromfohrländer",
  "Kumaon Mastiff",
  "Kunming Wolfdog",
  "Kurī",
  "Kuvasz",
  "Kyi-Leo",
  "Labrador Husky",
  "Labrador Retriever",
  "Lagotto Romagnolo",
  "Lakeland Terrier",
  "Lancashire Heeler",
  "Landseer",
  "Lapponian Herder",
  "Leonberger",
  "Lhasa Apso",
  "Lithuanian Hound",
  "Löwchen",
  "Mackenzie River Husky",
  "Magyar agár",
  "Mahratta Greyhound",
  "Majorca Ratter",
  "Majorca Shepherd Dog",
  "Maltese",
  "Manchester Terrier",
  "Maremma Sheepdog",
  "McNab",
  "Mexican Hairless Dog",
  "Miniature Australian Shepherd",
  "Miniature American Shepherd",
  "Miniature Fox Terrier",
  "Miniature Pinscher",
  "Miniature Schnauzer",
  "Miniature Shar Pei",
  "Mioritic",
  "Molossus",
  "Molossus of Epirus",
  "Montenegrin Mountain Hound",
  "Moscow Watchdog",
  "Moscow Water Dog",
  "Mountain Cur",
  "Mucuchies",
  "Mudhol Hound",
  "Mudi",
  "Münsterländer, Large",
  "Münsterländer, Small",
  "Murcian Ratter",
  "Neapolitan Mastiff",
  "Newfoundland",
  "New Zealand Heading Dog",
  "Norfolk Spaniel",
  "Norfolk Terrier",
  "Norrbottenspets",
  "North Country Beagle",
  "Northern Inuit Dog",
  "Norwegian Buhund",
  "Norwegian Elkhound",
  "Norwegian Lundehund",
  "Norwich Terrier",
  "Nova Scotia Duck-Tolling Retriever",
  "Old Croatian Sighthound",
  "Old Danish Pointer",
  "Old English Sheepdog",
  "Old English Terrier",
  "Old German Shepherd Dog",
  "Old Time Farm Shepherd",
  "Olde English Bulldogge",
  "Otterhound",
  "Pachon Navarro",
  "Pandikona Hunting Dog",
  "Paisley Terrier",
  "Papillon",
  "Parson Russell Terrier",
  "Patterdale Terrier",
  "Pekingese",
  "Perro de Presa Canario",
  "Perro de Presa Mallorquin",
  "Peruvian Hairless Dog",
  "Phalène",
  "Pharaoh Hound",
  "Phu Quoc Ridgeback",
  "Picardy Spaniel",
  "Plummer Terrier",
  "Plott Hound",
  "Podenco Canario",
  "Pointer",
  "Poitevin",
  "Polish Greyhound",
  "Polish Hound",
  "Polish Hunting Dog",
  "Polish Lowland Sheepdog",
  "Polish Tatra Sheepdog",
  "Pomeranian",
  "Pont-Audemer Spaniel",
  "Poodle",
  "Porcelaine",
  "Portuguese Podengo",
  "Portuguese Pointer",
  "Portuguese Water Dog",
  "Posavac Hound",
  "Pražský Krysařík",
  "Pudelpointer",
  "Pug",
  "Puli",
  "Pumi",
  "Pungsan Dog",
  "Pyrenean Mastiff",
  "Pyrenean Shepherd",
  "Rafeiro do Alentejo",
  "Rajapalayam",
  "Rampur Greyhound",
  "Rastreador Brasileiro",
  "Ratonero Bodeguero Andaluz",
  "Ratonero Valenciano",
  "Rat Terrier",
  "Redbone Coonhound",
  "Rhodesian Ridgeback",
  "Rottweiler",
  "Russian Spaniel",
  "Russian Toy",
  "Russian Tracker",
  "Russo-European Laika",
  "Russell Terrier",
  "Saarloos Wolfdog",
  "Sabueso Español",
  "Sabueso fino Colombiano",
  "Saint-Usuge Spaniel",
  "Sakhalin Husky",
  "Saluki",
  "Samoyed",
  "Sapsali",
  "Šarplaninac",
  "Schapendoes",
  "Schillerstövare",
  "Schipperke",
  "Standard Schnauzer",
  "Schweizer Laufhund",
  "Schweizerischer Niederlaufhund",
  "Scotch Collie",
  "Scottish Deerhound",
  "Scottish Terrier",
  "Sealyham Terrier",
  "Segugio Italiano",
  "Seppala Siberian Sleddog",
  "Serbian Hound",
  "Serbian Tricolour Hound",
  "Seskar Seal Dog",
  "Shar Pei",
  "Shetland Sheepdog",
  "Shiba Inu",
  "Shih Tzu",
  "Shikoku",
  "Shiloh Shepherd",
  "Siberian Husky",
  "Silken Windhound",
  "Sinhala Hound",
  "Skye Terrier",
  "Sloughi",
  "Slovak Cuvac",
  "Slovakian Rough-haired Pointer",
  "Slovenský Kopov",
  "Smålandsstövare",
  "Small Greek Domestic Dog",
  "Soft-Coated Wheaten Terrier",
  "South Russian Ovcharka",
  "Southern Hound",
  "Spanish Mastiff",
  "Spanish Water Dog",
  "Spinone Italiano",
  "Sporting Lucas Terrier",
  "St. Bernard",
  "St. John's Water Dog",
  "Stabyhoun",
  "Staffordshire Bull Terrier",
  "Stephens Cur",
  "Styrian Coarse-haired Hound",
  "Sussex Spaniel",
  "Swedish Lapphund",
  "Swedish Vallhund",
  "Tahltan Bear Dog",
  "Taigan",
  "Taiwan Dog",
  "Talbot",
  "Tamaskan Dog",
  "Teddy Roosevelt Terrier",
  "Telomian",
  "Tenterfield Terrier",
  "Terceira Mastiff",
  "Thai Bangkaew Dog",
  "Thai Ridgeback",
  "Tibetan Mastiff",
  "Tibetan Spaniel",
  "Tibetan Terrier",
  "Tornjak",
  "Tosa",
  "Toy Bulldog",
  "Toy Fox Terrier",
  "Toy Manchester Terrier",
  "Toy Trawler Spaniel",
  "Transylvanian Hound",
  "Treeing Cur",
  "Treeing Tennessee Brindle",
  "Treeing Walker Coonhound",
  "Trigg Hound",
  "Tweed Water Spaniel",
  "Tyrolean Hound",
  "Uruguayan Cimarron",
  "Valencian Ratter",
  "Vanjari Hound",
  "Villano de las Encartaciones",
  "Vizsla",
  "Volpino Italiano",
  "Weimaraner",
  "Welsh Corgi, Cardigan",
  "Welsh Corgi, Pembroke",
  "Welsh Sheepdog",
  "Welsh Springer Spaniel",
  "Welsh Terrier",
  "West Highland White Terrier",
  "West Siberian Laika",
  "Westphalian Dachsbracke",
  "Wetterhoun",
  "Whippet",
  "White Shepherd",
  "Wirehaired Pointing Griffon",
  "Wirehaired Vizsla",
  "Xiasi Dog",
  "Yorkshire Terrier",
]

def add_dog_breeds():
    for breed in dog_breeds:
        breeds.insert_one ({
            "id": str(uuid.uuid4()),
            "value": breed
        })


dog_thumbnails = [
    "/static/img/sample_dogs/01f3e1c841cf3b864ea024d8eb0c7251--dog-pictures-animal-pictures.jpg",
    "/static/img/sample_dogs/630f0ef3f6f3126ca11f19f4a9b85243--dachshund-puppies-weenie-dogs.jpg",
    "/static/img/sample_dogs/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg",
    "/static/img/sample_dogs/bordercollie1.jpg",
    "/static/img/sample_dogs/Common-dog-behaviors-explained.jpg",
    "/static/img/sample_dogs/dog-1210559_960_720.jpg",
    "/static/img/sample_dogs/dog-bone.png",
    "/static/img/sample_dogs/dog-breed-selector-australian-shepherd.jpg",
    "/static/img/sample_dogs/file_23252_dogue-de-bordeaux-dog-breed.jpg",
    "/static/img/sample_dogs/German-Shepherd-Dog-1.jpg",
    "/static/img/sample_dogs/labrador-retriever1istock.jpg",
    "/static/img/sample_dogs/Natural-Dog-Law-2-To-dogs,-energy-is-everything.jpg",
    "/static/img/sample_dogs/pexels-photo-356378.jpeg",
    "/static/img/sample_dogs/scroll000.jpg",
    "/static/img/sample_dogs/scroll0011.jpg",
    "/static/img/sample_dogs/thul-571a0332-3d53-51bc-8189-e2a4771f3470.jpg",
    "/static/img/sample_dogs/wildlife-photography-pet-photography-dog-animal-159541.jpeg"
]


dog_colors = [
    "brown",
    "blue",
    "asian",
    "whitest",
    "tan",
    "brown with spots",
    "kind of purpley",
    "steel blue"
]

dog_genders = ["male", "female"]

dog_bool = ["yes", "no"]

dog_ears = [
    "stand-up",
    "cropped",
    "folded"
]

def get_thumbnail():
    stop = len(dog_thumbnails)
    rand = random.randrange(0,stop)
    return dog_thumbnails[rand]

def get_breed():
    stop = len(dog_breeds)
    rand = random.randrange(0, stop)
    return dog_breeds[rand]

def get_id():
    return random.randrange(0,999999)

def get_color():
    stop = len(dog_colors)
    rand = random.randrange(0, stop)
    return dog_colors[rand]

def get_age():
    return random.randrange(0,15)

def datetimeconverter(n):
    #front end date input(n) is always formated {%Y}-{%m}-{%d}
    #converts to datetime object
    return datetime.strptime(n, '%Y-%m-%d')

def get_date():
    day = random.randrange(1,31)
    month = random.randrange(1,12)
    year = random.randrange(2016,2017)
    date = "{}-{}-{}".format(year,month,day)
    return datetimeconverter(date)

def get_height_weight():
    return random.randrange(5,69)

def get_bool(x):
    rand = bool(random.getrandbits(1))
    if rand:
        rand = 0
    else:
        rand = 1
    if x == "bool":
        return dog_bool[rand]
    elif x == "gend":
        return dog_genders[rand]
def get_ears():
    stop = len(dog_ears)
    rand = random.randrange(0,stop)
    return dog_ears[rand]

def get_note():
    nouns = ("puppy", "pooch", "doggy dog", "monster", "service dog")
    verbs = ("ran", "vanished", "disappeared", "exploded", "stole away")
    adv = ("randomly", "vapidly", "foolishly", "merrily", "again")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    num = random.randrange(0,5)
    return "My {} {} {} {}.".format(adj[num],nouns[num],verbs[num],adv[num])

def bulk_add_dogs():
    for name in dog_names:
        _id = str(uuid.uuid4())
        dogs.insert_one(
            {
            "_id": _id,
            "dog_name": name,
            "thumbnail": get_thumbnail(),
            "breed": get_breed(),
            "id_chip": get_id(),
            "age": get_age(),
            "date_found": get_date(),
            "location_found": "Houston",
            "prim_color": get_color(),
            "sec_color": get_color(),
            "height": get_height_weight(),
            "weight": get_height_weight(),
            "gender": get_bool("gend"),
            "fix": get_bool("bool"),
            "collar": get_bool("bool"),
            "collar_color": get_color(),
            "ears": get_ears(),
            "eyes": get_color(),
            "notes": get_note(),
            "delete": False
            }
        )
        dog = dogs.find({
        "_id": _id
        })

        for dog in dog:
            name = dog['dog_name']
            gender = dog['gender']
            if gender == "male":
                gender = "He"
            else:
                gneder = "She"
            breed = dog['breed']
            age = dog['age']
            print("Added {} to the DB. {} is a {} year old {}.".format(name, gender, age, breed))

bulk_add_dogs()
