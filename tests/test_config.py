import pytest
import logging
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range":
        {
            "Item_Weight": 30,
            "Item_Fat_Content": 2,
            "Item_Visibility": 4,
            "Item_Type": 2,
            "Item_MRP": 300,
            "Outlet_Establishment_Year": 2020,
            "Outlet_Size": 1,
            "Outlet_Location_Type": 0,
            "Outlet_Type": 1
        },

    "correct_range":
        {
            "Item_Weight": 9,
            "Item_Fat_Content": 1,
            "Item_Visibility": 0.00012,
            "Item_Type": 2,
            "Item_MRP": 35,
            "Outlet_Establishment_Year": 1999,
            "Outlet_Size": 1,
            "Outlet_Location_Type": 0,
            "Outlet_Type": 1
        }
}

TARGET_range = {
    "min": 33.29,
    "max": 13086.9648
}


def test_form_response_correct_range(data=input_data["correct_range"]):
    response = form_response(data)
    assert TARGET_range["min"] <= response <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    response = form_response(data)
    assert response["response"] == prediction_service.prediction.NotInRange().message


#def test_form_response_correct_range(data=input_data["correct_range"]):
 #   response = api_response(data)
  #  print(response)
   # assert TARGET_range["min"] <= response <= TARGET_range["max"]

#def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
 #   response = api_response(data)
 # assert response["response"] == prediction_service.prediction.NotInRange().message

