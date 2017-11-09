import argparse
import lstm2
import numpy as np
# fix random seed for reproducibility
np.random.seed(7)

'''
Read config file and set up variables 
'''

parser = argparse.ArgumentParser(description='Create multi-variate LSTM models')
parser.add_argument('config_file', nargs='?', help='config_file to use')

args = parser.parse_args()
print('Reading' + args.config_file)

source_dir, models_dir, supervised_data_dir, prediction_data_dir, rmse_csv,n_lags, n_forecast, n_test = lstm2.read_config(args.config_file)

'''
Now generate supervised data
'''
n_features, datasets = lstm2.set_up_data(source_dir, supervised_data_dir, n_lags, n_forecast)

'''
Train models
'''
histories = lstm2.build_models(supervised_data_dir, models_dir, n_test, n_lags, n_features)