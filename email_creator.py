import csv
from pathlib import Path
import os
from email_sender import send_email
import re
current_dir = os.getcwd()

name_list = []
address_list = []
phone_number_list = []
email_list = []
social_security_list = []
order_id_list = []


def parse_file():
    file = current_dir+"/Amazon_Returns.txt"
    with open(file, "r") as fr:
        next(fr)
        for each_line in fr.readlines():
            each_line = each_line.strip()
            contains_address(each_line)
            contains_name(each_line)
            contains_phone_number(each_line)
            contains_email(each_line)
            contains_social_security(each_line)
        '''
        if len(name_list) > 0 or len(address_list) > 0 or len(phone_number_list) > 0 or len(email_list) > 0 or len(social_security_list) > 0:
        '''
        if pi == True:
            EMAIL_TEMPLATE = "Dear Amazon Returns Team,\n\
            This email is being sent out in order to notify you that personal information was found,\n\
            and thus might have been subject to a data breach.\n\
            This personal information was redacted and the file was updated.\n\
            Here is a list of all the Order IDs which contained Personal Information:\n\
                Order ID: {order_list}\n\
Thank you.".format(order_list=order_id_list)
            send_email(body=EMAIL_TEMPLATE, subject="Data Breach")

def contains_name(input):
    name = re.findall(r'([a-zA-Z]+\s+[a-zA-z]+)', input)
    pattern = '<REDACTED>'
    if len(name) > 0:
        order = re.findall(r'(\d{1}-\d{1}-\d{1})',input)
        for item in order:
            order_id_list.append(item)
        for each_item in name:
            name_list.append(each_item)
        with open(r'Amazon_Returns.txt', 'r') as file:
            data = file.read()
            for each in name_list:
                data = data.replace(str(each), pattern)
        with open(r'Amazon_Returns.txt', 'w') as file:
            file.write(data)

def contains_address(input):
    address = re.findall(r'(\d{4}.*?\s+.+\d{5})', input)
    pattern = '<REDACTED>'
    if len(address) > 0:
        order = re.findall(r'(\d{1}-\d{1}-\d{1})', input)
        for item in order:
            order_id_list.append(item)
        for each_item in address:
            address_list.append(each_item)
        with open(r'Amazon_Returns.txt', 'r') as file:
            data = file.read()
            for each in address_list:
                data = data.replace(str(each), pattern)
        with open(r'Amazon_Returns.txt', 'w') as file:
            file.write(data)

def contains_phone_number(input):
    phone_number = re.findall(r'(\d{3}-\d{3}-\d{4})', input)
    pattern = '<REDACTED>'
    if len(phone_number) > 0:
        order = re.findall(r'(\d{1}-\d{1}-\d{1})', input)
        for item in order:
            order_id_list.append(item)
        for each_item in phone_number:
            phone_number_list.append(each_item)
        with open(r'Amazon_Returns.txt', 'r') as file:
            data = file.read()
            for each in phone_number_list:
                data = data.replace(str(each), pattern)
        with open(r'Amazon_Returns.txt', 'w') as file:
            file.write(data)

def contains_email(input):
    email = re.findall(r'([\S]+@[\w]+(?:\.[\w]+)+)', input)
    pattern = '<REDACTED>'
    if len(email) > 0:
        order = re.findall(r'(\d{1}-\d{1}-\d{1})', input)
        for item in order:
            order_id_list.append(item)
        for each_item in email:
            email_list.append(each_item)
        with open(r'Amazon_Returns.txt', 'r') as file:
            data = file.read()
            for each in email_list:
                data = data.replace(str(each), pattern)
        with open(r'Amazon_Returns.txt', 'w') as file:
            file.write(data)

def contains_social_security(input):
    social_security = re.findall(r'(\d{3}-\d{2}-\d{4})', input)
    pattern = '<REDACTED>'
    if len(social_security) > 0:
        order = re.findall(r'(\d{1}-\d{1}-\d{1})', input)
        for item in order:
            order_id_list.append(item)
        for each_item in social_security:
            social_security_list.append(each_item)
        with open(r'Amazon_Returns.txt', 'r') as file:
            data = file.read()
            for each in social_security_list:
                data = data.replace(str(each), pattern)
        with open(r'Amazon_Returns.txt', 'w') as file:
            file.write(data)


if __name__ == "__main__":
    parse_file()


