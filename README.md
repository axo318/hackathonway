# hackathonway

<b>System Description:<b>

1. Collect symptoms and personal details
2. Keep waiting patients in memory (each gets random identtifier) and order them with priority

-- Doctor sees the patient and diagnoses --

3. Doctor inputs diagnosis
4. Predict probability of diagnosis being wrong (based on automatic diagn, based on doctor accuracy record)
5. If high probability -> Recommend a second opinion from an expert in recommended field



<b>Docs:<b>

* Structures
	* Person
		* Patient
		* Doctor
	* Ticket
	* Symptom
	* Diagnosis
	* Disease

* Controllers
	* Controller
	* PatientQueue
	* 