# hotdog not hotdog  <a href="url"><img src="http://www.emoji.co.uk/files/apple-emojis/food-drink-ios/381-hot-dog.png"  height="48" width="48" ></a>

## Inspired from Silicon Valley tv show's Entrepreneur in residence Jiyan Yang's app 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ACmydtFDTGs/0.jpg)](https://www.youtube.com/watch?v=ACmydtFDTGs)



* Demo - URL


* Here is an image classifier built to learn about various food types - including Hotdogs, Burgers, Pizza and Sandwiches. 


*  Unless image has high inclination to Hotdog I'm not marking it as hotdog. 


* Training it only on hotdog was giving lower accuracy than training it on various similar food items and checking if the food item is a hotdog 

* Tensorflow is used to retrain MobileNet with a concept called Transfer learning. 
  * MobileNets are optimized to be small and efficient, at the cost of some accuracy, when compared to other pre-trained models
  * Transfer Learning, means starting with a model that has been already trained on another problem. Deep learning from scratch can take days, but transfer learning can be done in short order.

* List of all [Pre-trained models](https://github.com/tensorflow/models/tree/master/slim#pre-trained-models) one can use to build an image classifier depending on usage and compute available


*  Demo hosted on Google App Engine using Flask 


## Potential
* Product #1: With enough training size and compute strength - Anyone can extend this to create the See-food App/ Shazam for food
* Product #2: Tie food to ingredients - knowing habits of food preference Amazon can reccomend ingredients when they look for food on Yelp. 
* Product #3: Knowing your allergies an app can point camera to the food and we lookup ingredients and warn the user
