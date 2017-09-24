# hotdog not hotdog  <a href="url"><img src="http://www.emoji.co.uk/files/apple-emojis/food-drink-ios/381-hot-dog.png"  height="48" width="48" ></a>

## Inspired from Silicon Valley tv show's Entrepreneur in residence Jiyan Yang's app 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ACmydtFDTGs/0.jpg)](https://www.youtube.com/watch?v=ACmydtFDTGs)


Here is an image classifier - which reads an uploaded image to classify as a hotdog or a not hotdog 


### Demo - https://hotdog-not-hotdog.appspot.com/

 

## Working


* Thanks to google's codelab demos of tensorflow for image classification [link](https://codelabs.developers.google.com/). 


* I fetched images fortwo categories
  -  hotdog
  -  non hotdogs included various other images like - sandwiches, pizzas, salads, pasta, movie covers, wallpapers etc to cover wide variety of images.


* Tensorflow is used to retrain MobileNet with a concept called Transfer learning. 
  * MobileNets are optimized to be small and efficient, at the cost of some accuracy, when compared to other pre-trained models
  * Transfer Learning, means starting with a model that has been already trained on another problem. Deep learning from scratch can take days, but transfer learning can be done in short order.

* Once model is ready, google has tricks to reduce the size of the model
  * tf includes a tool called optimize_for_inference, that removes all nodes that aren't needed for a given set of input and outputs.
  * The script also does a few other optimizations that help speed up the model, such as merging explicit batch normalization operations into the convolutional weights to reduce the number of calculations.
  * The second script called quantize_graph is available for optimization which quantizes the weight of the network allowing 


* List of all [Pre-trained models](https://github.com/tensorflow/models/tree/998104bfdf14f74a2398e951325e4660862c5f20/slim#pre-trained-models) one can use to build an image classifier depending on usage and compute available


*  Demo hosted on [Google App Engine](https://cloud.google.com) using Flask
   * Images hoted on google bucket 
   * Images extracted from google images using Fatkun Batch Download Image


## Potential
* Product #1: With enough training size and compute strength - Anyone can extend this to create the See-food App/ Shazam for food
* Product #2: Tie food to ingredients and enable AI- "Alexa get ingredients for Risotto for six people on friday" 
* Product #3: Knowing your allergies an app can point camera to the food and we lookup ingredients and warn the user
