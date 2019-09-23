""" Checks for resource existence"""
from rest_framework import status
from recipe_app.helpers.error_message import ERROR_MESSAGES


def resource_exists(model, column_name, column_value, **kwargs):
    """Checks if resource exists."""

    try:
        model_instance = model.objects.get(**{column_name: column_value})
        return model_instance
    except model.DoesNotExist:
        False

    
    
def get_response(**kwargs):
    """Creates response body"""

    msg_type = kwargs.get('res_type', 'error')
    response = {'status': msg_type}
    if msg_type == 'error':
        error_key = kwargs.get('error_key')
        error = ERROR_MESSAGES.get(error_key)
        format_str = kwargs.get('format_str')
        body = {
            'error': error[0].format(format_str),
            'message': error[1].format(format_str),
        }
    else:
        body = {'data': kwargs.get('data')}
    response.update(body)

    return response



def save_serializer(serializer):
    """returns a particular response for when serializer passed is valid or not
    Helper function to save serializer """
    serializer.save()
    data = {
        "status": "success",
        "data": serializer.data
    }
    return data


def check_resource(model, model_serializer, column_name, column_value, request, model_name):
    """
        returns a particular message for when resource exist or not.
    """
    try:
        resource = model.objects.get(**{column_name: column_value})
        if request.method == "GET":
            serializer = model_serializer(
                resource, context={'request': request})
            data = {
                'status': 'success',
                'data': serializer.data
            }
            return (data, status.HTTP_200_OK)
        serializer = model_serializer(
            resource, context={'request': request}, data=request.data, partial=True)
        if serializer.is_valid():
            data = save_serializer(serializer)
            return (data, status.HTTP_200_OK)
        data = {
            "status": "error",
            "error": "name is empty",
            "message": "Ensure the name is not empty"
        }
        return (data, status.HTTP_400_BAD_REQUEST)
    except model.DoesNotExist:
        data = {
            'status': 'error',
            'error': '{}_not_found.'.format(model_name),
            'message': 'Ensure the ID passed is of an existing {}.'.format(model_name)
        }
        return (data, status.HTTP_404_NOT_FOUND)
