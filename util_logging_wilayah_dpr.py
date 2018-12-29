import logging

def pecker(file_name, message_string):
	logging.basicConfig(filename='log_wilayah_ALL_DATA.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
	logging.warning(message_string)

	# logging.basicConfig(filename=file_name, filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
	# logging.warning(message_string)

	# formatter = logging.Formatter('%(asctime)s - %(message)s','%d-%b-%y %H:%M:%S')

	# handler_any = logging.FileHandler('log_ALL_DATA.log')
	# handler_any.setFormatter(formatter)
	# logger_any = logging.getLogger('any_data')
	# logger_any.setLevel(logging.INFO)
	# logger_any.addHandler(handler_any)
	# logger_any.info(message_string)

	# handler = logging.FileHandler(file_name)
	# handler.setFormatter(formatter)
	# logger = logging.getLogger(file_name)
	# logger.setLevel(logging.INFO)
	# logger.addHandler(handler)
	# logger.info(message_string)


	return
