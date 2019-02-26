from keras.models import load_model
import sys

model = ""

if(len(sys.argv) > 2 and sys.argv[2] == 'loadmodel'):
    model = load_model('main_app/ecgScratchEpoch2.hdf5')
    model._make_predict_function()          # Necessary
    print('Model loaded. Start serving...')
