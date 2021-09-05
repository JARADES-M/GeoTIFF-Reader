from services import image_processor

def test_get_local_datetime_from_filename_success():
    file_name = '319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif'
    expected = '2016-12-07T15:19:53-02:00'
    result = image_processor.get_local_datetime_from_filename(file_name, -47.597228921551284, -15.858576386589299)
    assert result == expected

def test_get_timezone_from_lng_lat_success():
    expected = 'America/Sao_Paulo'
    result = image_processor.get_timezone_from_lng_lat(-47.597228921551284, -15.858576386589299)
    assert result == expected