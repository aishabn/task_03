from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [

    		{"restaurant_name" : "tatami",
    		"food_type" : "sushi"},

    		{"restaurant_name" : "burger club",
    		"food_type" : "burger"},

    		{"restaurant_name" : "solo",
    		"food_type" : "pizza"},


    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    		"my_object" : {"restaurant_name" : "tatami",
    						"food_type" : "sushi"}

    }
    return render(request, 'detail.html', context)
