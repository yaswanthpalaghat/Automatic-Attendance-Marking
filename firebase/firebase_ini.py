import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import storage;


def upload_file(filename):
    cred=credentials.Certificate('firebase/yaswanth-937ae-firebase-adminsdk-rlevj-37b865d23f.json');
    default_app=firebase_admin.initialize_app(cred,{
        'storageBucket': 'yaswanth.appspot.com'
    });
    bucket=storage.bucket();

    uploadBlob = bucket.blob('attendance/'+filename);
    #uploadBlob = bucket.get_blob('attendance2018-09-10.xls');
    print(uploadBlob);
    uploadBlob.upload_from_filename(filename='firebase/attendance_files/'+filename);
    print('file uploaded! ');
