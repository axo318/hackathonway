# This file will give methods on extracting the hamming distance given a symptom list

import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.special import softmax
import os
from config import dis_ids, symp_ids, syms_dis_weights, diagnosis_amount_df



class SimilarityModel():

    def __init__(self):
        self._create_model()
        self.MOST_SIMILAR_SYMPTOM = ""
        self.WEIGHT = 0.0

    def _create_model(self):
        # for each diagnosis have entry of symptom ids
        # new columns = diagnosis, symptom ids, weight of disease !!!!!!!!!!!!!!!!
        # check how mnay values of weights assigned to each diagnosis
        final_entries = []
        # for each disease id get entries of symptoms n weight
        for i,x in enumerate(dis_ids['id'].unique()):
            symtom_ids = syms_dis_weights[syms_dis_weights.did.isin([x])]['syd'].tolist()
            weights = syms_dis_weights[syms_dis_weights.did.isin([x])]['wei'].tolist()
            if len(weights)>0:
                weight_av = sum(weights)/len(weights)
            final_entries.append([x, symtom_ids, weight_av])

        final_df = pd.DataFrame(final_entries)
        final_df.columns = ['Diagnosis', 'Symptoms', 'Weight']

        # Putting words instead of ids
        for i,x in enumerate(final_df['Diagnosis']):
            final_df['Diagnosis'].loc[i] = dis_ids.loc[(dis_ids['id'] == x)]['title'].values

        for i,x in enumerate(final_df['Symptoms']):
            sympnames = []
            for sympid in x:
                if len(symp_ids.loc[(symp_ids['_id'] == sympid)]['symptom'].tolist())>0:
                    sympnames.append(symp_ids.loc[(symp_ids['_id'] == sympid)]['symptom'].tolist()[0])
            final_df['Symptoms'].loc[i] = sympnames

        final_df['Weight'] = final_df['Weight'].round(2)

        for i,x in enumerate(final_df['Diagnosis']):
            if len(x)>0:
                wds = x[0].split()
                seperator = " "
                clean = seperator.join(wds)
            final_df['Diagnosis'].loc[i] = clean

        for x in final_df['Symptoms']:
            if len(x)>0:
                for w in x:
                    wds = w.split()
                    seperator = " "
                    clean = seperator.join(wds)
            final_df['Symptoms'].loc[i] = clean

        final_df = final_df[final_df['Diagnosis'] != "Premature ejaculation"]
        final_df = final_df[final_df.astype(str)['Symptoms'] != '[]']

        diagnosis_amount = diagnosis_amount_df[["name","diagnosis_count"]]

        symptoms = final_df.Symptoms

        symptoms_set = set(x for l in symptoms for x in l)
        symptoms_list = list(symptoms_set)
        symptoms_list[0:3]

        symptoms_dataframe = pd.DataFrame(columns=symptoms_list)
        counter = 0

        for diagnosis in final_df.Diagnosis:
            symptoms = final_df.loc[final_df['Diagnosis'] == diagnosis].Symptoms
            symptoms_set = set(x for l in symptoms for x in l)
            symptoms_temp_list = list(symptoms_set)
            sym_num_list = list()
            for symptom in symptoms_dataframe.columns:
                if (symptom in symptoms_temp_list):
                    sym_num_list.append(1)
                else:
                    sym_num_list.append(0)

            # add list to dataframe
            symptoms_dataframe.loc[counter] = (sym_num_list)
            counter += 1

        frames = [symptoms_dataframe, final_df.Diagnosis, final_df.Weight]

        symptoms_dataframe["Diagnosis"] = final_df.Diagnosis
        symptoms_dataframe["Weight"] = final_df.Weight
        symptoms_dataframe = symptoms_dataframe.dropna()

        self.dataframe = symptoms_dataframe

    def _get_similarity_dataframe(self, symptoms_vector):
        similarity_df = pd.DataFrame(columns=["Diagnosis","Similarity", "Weight"])
        counter = 0
        for index, row in self.dataframe.iterrows():
            row = row[:-2]
            similarity = distance.hamming(row,symptoms_vector)
            similarity_df.loc[index] = [self.dataframe.Diagnosis[index], similarity, self.dataframe.Weight[index]]
            counter += 1
        similarity_df = similarity_df.sort_values(by="Similarity", ascending=False)
        # --
        self.MOST_SIMILAR_SYMPTOM = similarity_df.Similarity.values[:-1]
        self.WEIGHT = similarity_df.Weight.values[:-1]
        # --
        return similarity_df

    # create a valid symptom vector from a list of symptoms
    def _create_symptoms_vector(self, symptoms):
        stored_symptoms = self.dataframe.columns[:-2]
        symptoms = list(set(symptoms))
        vector = []
        # pre-fill vector with 0's
        for idx in range(len(stored_symptoms)):
            vector.append(0)

        # populate vector with appearance of symptom
        for idx, sym in enumerate(stored_symptoms):
                if (sym in symptoms):
                    vector[idx] = 1
        return vector


    # get a similarity dataframe where the bottom is the most similar
    def get_similarity(self, symptoms):
        vector = self._create_symptoms_vector(symptoms)
        similarity_dataframe = self._get_similarity_dataframe(vector)
        prob_dataframe = self._get_probability_dataframe(similarity_dataframe)
        return prob_dataframe

    def _get_similarity_test(self):
        vector = self.dataframe.iloc[3][:-2]
        similarity_df = self._get_similarity_dataframe(vector)
        prob_dataframe = self._get_probability_dataframe(similarity_df)
        return prob_dataframe

    def _get_probability_dataframe(self, dataframe):
        similarities = dataframe["Similarity"]
        similarities = [1 - x for x in similarities]
        print("Similarities: {}".format(similarities))
        probabilities = softmax(similarities)
        print("probabilities: {}".format(probabilities))
        dataframe_prob = dataframe.copy().drop(columns=["Similarity"])
        dataframe_prob["Similarity Probability"] = probabilities
        # print(dataframe_prob)
        return dataframe_prob


def test_1(model):
    similarity_df = model._get_similarity_test()
    print(similarity_df.tail(5))

def test_2(model):
    symptoms = ["Unsteady gait (Trouble walking)","Confusion and headache", "Confusion", "Loss of balance"]
    similarity_df = model.get_similarity(symptoms)
    print(similarity_df.tail(5))

def test_3(model):
    symptoms = [""]
    similarity_df = model.get_similarity(symptoms)
    print(similarity_df.tail(5))

def test_4(model):
    symptoms = []
    similarity_df = model.get_similarity(symptoms)
    print(similarity_df.tail(5))

if __name__ == "__main__":
    model = SimilarityModel()
    test_1(model)
    test_2(model)
    test_3(model)
    test_4(model)
