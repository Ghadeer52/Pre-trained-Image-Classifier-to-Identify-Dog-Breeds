#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
##
# Imports python modules
from os import listdir
# TODO 2: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 2" for the get_pet_labels function 
#       Please be certain to replace None in the return statement with 
#       results_dic dictionary that you create with this function
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create an empty dictionary to store the results
    results_dic = {}
    # Get the list of files in the directory
    in_files = listdir(image_dir)
    # Iterate over the files in the directory
    for file_name in in_files:
        # Filter out hidden files
        if not file_name.startswith('.'):
            # Remove file extension
            pet_label = file_name.split('.')[0]
            # Split the file name by underscores
            words = pet_label.split('_')
            # Create an empty list to store the filtered words
            filtered_words = []
            # Iterate over the words and filter out words with digits
            for word in words:
                if not any(char.isdigit() for char in word):
                    filtered_words.append(word.lower())
            # Join the filtered words to form the pet label
            pet_label = ' '.join(filtered_words)
            # Strip leading/trailing whitespace characters from pet label
            pet_label = pet_label.strip()
            # Add the pet label to the dictionary
            results_dic[file_name] = [pet_label]
    return results_dic