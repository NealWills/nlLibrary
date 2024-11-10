from enum import Enum
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from books import models
from django.utils import timezone
import uuid

# Create your views here.

class RequestError(Enum):

    Error = (False, -1, 'Request failure')
    Success = (True, 0, 'Request success')

    Unvalid_book_id = (False, -100001, 'Request failure: book_id unvalid')
    Unvalid_book_name = (False, -100002, 'Request failure: book_name unvalid')
    Unvalid_book_user = (False, -100003, 'Request failure: book_user unvalid')
    Unvalid_book_type = (False, -100004, 'Request failure: book_type unvalid')
    Unvalid_book_content = (False, -100005, 'Request failure: book_content unvalid')
    Unvalid_book_ssin = (False, -100006, 'Request failure: book_ssin unvalid')
    Duplicate_book_ssin = (False, -100007, 'Request failure: book_ssin exist')
    BookNotExist_book_id = (False, -100008, 'Request failure: book not exist')
    BookAlreadyDelete_book_id = (False, -10009, 'Request failure: book already delete')
    BookAlreadyForeverDelete_book_id = (False, -100010, 'Request failure: book already forever delete')
    BookUpdateNothingChange = (False, -100010, 'Request failure: book update nothing change')

    def failureMapToDic(self):
        return {
            'status': self.value[0],
            'code': self.value[1],
            'msg': self.value[2]
        }
    
    def successMapToDic(self, data):
        return {
            'status': self.value[0],
            'code': self.value[1],
            'msg': self.value[2],
            'data': data
        }
    

@api_view(['PUT'])
def book_add(request):
    book_name = request.data.get('book_name')
    book_user = request.data.get('book_user')
    book_type = request.data.get('book_type')
    book_content = request.data.get('book_content')
    book_ssin = request.data.get('book_ssin')

    if is_non_empty_str(book_name) == False :
        return JsonResponse(RequestError.Unvalid_book_name.failureMapToDic())
    elif is_non_empty_str(book_user) == False : 
        return JsonResponse(RequestError.Unvalid_book_user.failureMapToDic())
    elif is_non_empty_str(book_type) == False : 
        return JsonResponse(RequestError.Unvalid_book_type.failureMapToDic())
    elif is_non_empty_int(book_ssin) == False : 
        return JsonResponse(RequestError.Unvalid_book_ssin.failureMapToDic())
    # elif models.Books.objects.filter( book_ssin = book_ssin ).exists():
    #    return JsonResponse(RequestError.Duplicate_book_ssin.failureMapToDic())
    

    default_book_id = str(uuid.uuid4()).replace('-', '') 
    default_time_now = timezone.now()

    dbBook = models.Books(
        book_name=book_name,
        book_user=book_user,
        book_type=book_type,
        book_content=book_content,
        book_ssin=book_ssin,
        book_id=default_book_id,
        is_delete=0,
        update_date=default_time_now,
        create_date=default_time_now,
        delete_date=default_time_now
    )
    dbBook.save()

    return JsonResponse(RequestError.Success.successMapToDic(data=dbBook.transToDic())) 



@api_view(['DELETE'])
def book_delete(request):
    bookId = request.data.get('book_id')
    if is_non_empty_str(bookId) == False:
        return JsonResponse(RequestError.Unvalid_book_id.failureMapToDic()) 
    
    if models.Books.objects.filter( book_id = bookId ).exists() == False:
        return JsonResponse(RequestError.BookNotExist_book_id.failureMapToDic()) 
    else: 
        bookItem = models.Books.objects.get( book_id = bookId) 
        if bookItem.is_delete == 1:
            return JsonResponse(RequestError.BookAlreadyDelete_book_id.failureMapToDic()) 
        elif bookItem.is_delete == 2:
            return JsonResponse(RequestError.BookAlreadyForeverDelete_book_id.failureMapToDic()) 
        else:
            if bookItem.book_id == '-1':
                bookItem.book_id = str(uuid.uuid4()).replace('-', '')
            bookItem.is_delete = 1
            bookItem.delete_date = timezone.now()
            bookItem.save()
            return JsonResponse(RequestError.Success.successMapToDic(data=bookItem.transToDic())) 



@api_view(['DELETE'])
def book_delete_forever(request):
    bookId = request.data.get('book_id')
    if is_non_empty_str(bookId) == False:
        return JsonResponse(RequestError.Unvalid_book_id.failureMapToDic()) 
     
    if models.Books.objects.filter( book_id = bookId ).exists() == False:
        return JsonResponse(RequestError.Unvalid_book_id.failureMapToDic()) 
    else: 
        bookItem = models.Books.objects.get( book_id = bookId) 
        if bookItem.is_delete == 2:
            return JsonResponse(RequestError.BookAlreadyForeverDelete_book_id.failureMapToDic())  
        else:
            if bookItem.book_id == '-1':
                bookItem.book_id = str(uuid.uuid4()).replace('-', '')
            bookItem.is_delete = 2
            bookItem.save()
            return JsonResponse(RequestError.Success.successMapToDic(data=bookItem.transToDic()))  



@api_view(['GET'])
def book_get(request):
    bookId = request.data.get('book_id')
    if is_non_empty_str(bookId) == False:
        return JsonResponse(RequestError.Unvalid_book_id.failureMapToDic())  
     
    if models.Books.objects.filter( book_id = bookId ).exists() == False:
        return JsonResponse(RequestError.BookNotExist_book_id.failureMapToDic())  
    else: 
        bookItem = models.Books.objects.get( book_id = bookId) 
        if bookItem.is_delete == 1:
            return JsonResponse(RequestError.BookAlreadyDelete_book_id.failureMapToDic()) 
        elif bookItem.is_delete == 2:
            return JsonResponse(RequestError.BookAlreadyForeverDelete_book_id.failureMapToDic()) 
        else:
            return JsonResponse(RequestError.Success.successMapToDic(data=bookItem.transToDic())) 


@api_view(['POST'])
def book_update(request):
    bookId = request.data.get('book_id')
    book_name = request.data.get('book_name')
    book_user = request.data.get('book_user')
    book_type = request.data.get('book_type')
    book_content = request.data.get('book_content')
    book_ssin = request.data.get('book_ssin')
    is_delete = request.data.get('is_delete')

    if is_non_empty_str(bookId) == False:
        return JsonResponse({'status': False, 'code': -1, 'msg': 'Book_id is unvalid'})             
    elif models.Books.objects.filter( book_id = bookId ).exists() == False:
        return JsonResponse(RequestError.Unvalid_book_id.failureMapToDic()) 
    
    anyChange = False

    bookItem = models.Books.objects.get( book_id = bookId)  
    if is_non_empty_str(book_name):
        bookItem.book_name = book_name
        anyChange = True
    if is_non_empty_str(book_user):
        bookItem.book_user = book_user
        anyChange = True
    if is_non_empty_str(book_type):
        bookItem.book_type = book_type 
        anyChange = True
    if is_non_empty_str(book_content):
        bookItem.book_content = book_content 
        anyChange = True
    if is_non_empty_int(book_ssin):
       bookItem.book_ssin = book_ssin 
       anyChange = True
    if is_non_empty_int(is_delete):
       bookItem.is_delete = is_delete   
       anyChange = True
    if anyChange == False:
        return JsonResponse(RequestError.BookUpdateNothingChange.failureMapToDic())
    else:
        bookItem.save()
        bookItem.update_date = timezone.now()
        return JsonResponse(RequestError.Success.successMapToDic(data=bookItem.transToDic()))


def is_non_empty_int(var):
    return isinstance(var, int)

def is_non_empty_str(var):
    return isinstance(var, str) and var

