from django.shortcuts import render , get_object_or_404 
from django.views.generic import ListView ,DetailView
from django.http import Http404

from .models import Product


# LISTVIEW
# ListView using class

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"


# ListView using function

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
	'object_list' : queryset 
	}
	return render(request,"products/list.html",context)



# DETAILVIEW
# DetailView using class type1

# class ProductDetailView(DetailView):
	# queryset = Product.objects.all()
	# template_name = "products/details.html"
	
	# def get_context_dat(self,*args ,**kwargs):
	# 	context = super(Product_DetailView,self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	#context['abc'] = 123
	# 	return context

# DetailView using class type2

class ProductDetailView(DetailView):
	template_name = "products/details.html"

	def get_context_data(self,*args,**kwargs):
		context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context


	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("products doest exist")
		return instance
	


# DetailView using function

# def product_detail_view(request,pk=None, *args, **kwargs):
# 	#instance = Product.objects.get(pk=pk)
# 	instance = get_object_or_404(Product,pk=pk)
# 	context = {
# 	'object':instance
# 	}
# 	return render(request,"products/details.html",context)



# DetailView using function type 2

# def product_detail_view(request,pk=None, *args, **kwargs):

# 	try:
# 		instance =Product.objects.get(id=pk)
# 	except Product.DoesNotExist:
# 		print("no product exist")
# 		raise Http404("Product doesnt exist")
# 	except:
# 		print("huhh?")	
# 	context = {
# 	'object':instance
# 	}
# 	return render(request,"products/details.html",context)		


# DetailView using function type 3

# def product_detail_view(request,pk=None, *args, **kwargs):	
# 	print( args, kwargs)
# 	qs = Product.objects.filter(id=pk)
# 	if qs.exists() and qs.count()==1:
# 		instance = qs.first()	
# 	else:
# 		raise Http404("Product doent exist")

# 	context ={
# 	"object" : instance
# 	}
# 	return render(request,"products/details.html",context) 


# DetailView using function type 4

def product_detail_view(request, pk= None, *args, **kwargs):
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product doesnt exist")
	context ={
	"object" : instance
	}
	return render(request,"products/details.html",context)


#Featured listView


class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.featured()


#Featured DetailView

class ProductFeaturedDetailView(DetailView):
	template_name = "products/fdetails.html"

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.featured()



#Slug DetailView


class ProductSlugDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/details.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		instance = get_object_or_404(Product,slug=slug)
		if instance is None:
			raise Http404("products doest exist")
		return instance
	
