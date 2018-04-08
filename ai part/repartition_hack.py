import sqlite3
from math import*
import numpy
import scipy
from numpy import*
from scipy import spatial
import matplotlib.pyplot as plt


#Create connection to the db
db_name = 'test.db'
# Try to connect
	
conn = sqlite3.connect(db_name)
conn.text_factory = str
c = conn.cursor()

class Data:
	def __init__(self,jobs,goals):
		self.jobs = jobs
		self.goals = goals
		
class Job:
	def __init__(self,name,current_weight,recommended_weight,recommended_rank,max_growth,max_security,max_exploration,max_innovation,max_education):
		self.name = name
		self.current_weight = current_weight
		self.recommended_rank = recommended_rank;
		self.recommended_weight = recommended_weight;
		self.goals = [max_growth,max_security,max_exploration,max_innovation,max_education];
		self.max_growth = max_growth
		self.max_security = max_security
		self.max_exploration = max_exploration
		self.max_innovation = max_innovation
		self.max_education = max_education
		
class Goal:
	def __init__(self,name,value):
		self.name = name
		self.value = value


#Helper functions---------------------------------------------------------
def initialize_db(job_goals_values):
	# Create table
	c.execute('''CREATE TABLE goals
				 (uid real,name text, value text)''')
				 
	c.execute('''CREATE TABLE skills_recommendation
				 (uid real,skill text)''')
				 
	c.execute('''CREATE TABLE job_weight
				 (uid real,name text, 
				 current_weight real, 
				 current_rank real, 
				 recommended_weight real, 
				 recommended_rank real, 
				 max_growth real, 
				 max_security real, 
				 max_exploration real, 
				 max_innovation real, 
				 max_education real)''')

	# Insert a row of data into goals table
	c.execute("INSERT INTO goals VALUES (0,'Security',1)")
	c.execute("INSERT INTO goals VALUES (1,'Wealth',3)")
	c.execute("INSERT INTO goals VALUES (2,'Exploration',4)")
	c.execute("INSERT INTO goals VALUES (3,'Innovation',1)")
	c.execute("INSERT INTO goals VALUES (4,'Expansioin',1)")


	# Insert a row of data into job_weight
	c.execute("INSERT INTO job_weight VALUES (0,'Maintenance Worker',0.16,0,0.16,0,'%d','%d','%d','%d','%d')" %(job_goals_values[0][0],job_goals_values[0][1],job_goals_values[0][2],job_goals_values[0][3],job_goals_values[0][4]))
	c.execute("INSERT INTO job_weight VALUES (1,'Lead Process Planner',0.16,1,0.16,1,'%d','%d','%d','%d','%d')" %(job_goals_values[1][0],job_goals_values[1][1],job_goals_values[1][2],job_goals_values[1][3],job_goals_values[1][4]))
	c.execute("INSERT INTO job_weight VALUES (2,'Ressource Excavator',0.16,2,0.16,2,'%d','%d','%d','%d','%d')" %(job_goals_values[2][0],job_goals_values[2][1],job_goals_values[2][2],job_goals_values[2][3],job_goals_values[2][4]))
	c.execute("INSERT INTO job_weight VALUES (3,'Medic',0.16,3,0.16,3,'%d','%d','%d','%d','%d')" %(job_goals_values[3][0],job_goals_values[3][1],job_goals_values[3][2],job_goals_values[3][3],job_goals_values[3][4]))
	c.execute("INSERT INTO job_weight VALUES (4,'Harvester',0.16,4,0.16,4,'%d','%d','%d','%d','%d')" %(job_goals_values[4][0],job_goals_values[4][1],job_goals_values[4][2],job_goals_values[4][3],job_goals_values[4][4]))
	c.execute("INSERT INTO job_weight VALUES (5,'Gardien',0.16,5,0.16,5,'%d','%d','%d','%d','%d')" %(job_goals_values[5][0],job_goals_values[5][1],job_goals_values[5][2],job_goals_values[5][3],job_goals_values[5][4]))
		

	c.execute("INSERT INTO skills_recommendation VALUES (0,'Structure')")
	c.execute("INSERT INTO skills_recommendation VALUES (1,'Electricity')")
	c.execute("INSERT INTO skills_recommendation VALUES (2,'Machine')")
	c.execute("INSERT INTO skills_recommendation VALUES (3,'Problem Solving')")
	c.execute("INSERT INTO skills_recommendation VALUES (4,'Programming')")
	c.execute("INSERT INTO skills_recommendation VALUES (5,'Battle')")

	# Save (commit) the changes
	conn.commit()

def get_goal_value(uid,col):
	c.execute('SELECT ({coi}) FROM {tn} WHERE uid="{cn}"'.\
        format(coi=col, tn='goals', cn=uid))
	
	return c.fetchone()[0]	
	
def get_job_value(uid,col):
	c.execute('SELECT ({coi}) FROM {tn} WHERE uid="{cn}"'.\
		format(coi=col, tn='job_weight', cn=uid))
	return c.fetchone()[0]
	
def populate_jobs(job_count):
	jobs = []
	for i in range(0,job_count):
		name = get_job_value(i,"name");
		current_weight = get_job_value(i,"current_weight");
		current_rank = get_job_value(i,"current_rank");
		recommended_rank = get_job_value(i,"recommended_rank");
		recommended_weight = get_job_value(i,"recommended_weight");
		max_growth = get_job_value(i,"max_growth");
		max_security = get_job_value(i,"max_security");
		max_exploration = get_job_value(i,"max_exploration");
		max_innovation = get_job_value(i,"max_innovation");
		max_education = get_job_value(i,"max_education");
		job = Job(name,current_weight,recommended_weight,recommended_rank,max_growth,max_security,max_exploration,max_innovation,max_education)
		jobs.append(job)
	return jobs
	
def populate_goals(goals_count):
	goals = []
	for i in range(0,goals_count):
		name = get_goal_value(i,"name");
		value = get_goal_value(i,"value");
		goal = Goal(name,value)
		goals.append(goal)
	return goals	

def populate_goals_value():
	goals_array = []
	#Security, Wealth, Exploration, Innovation and Expansion
	goals_array.append([1,2,2,3,2])
	goals_array.append([1,1,1,3,4])
	goals_array.append([1,4,3,1,1])
	goals_array.append([3,3,1,2,1])
	goals_array.append([1,3,3,1,2])
	goals_array.append([5,2,1,1,1])
	return goals_array

	
def populate_skill_array():
	skills_array = []
	skills_array.append([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
	skills_array.append([1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0])
	skills_array.append([0,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0])
	skills_array.append([0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1])
	skills_array.append([0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0])
	skills_array.append([0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1])
	return skills_array
	
def populate_skill_dict():
	skill_dict = {}
	skill_name = ['Structure','Electricity','Machine','Problem Solving','Programming',
					'Battle','Geography','Planning','Project Management','Peace Keeping',
					'Geology','Materials','Research','Biology','Manual Labor','Health',
					'Cleaning','Pharmacy','Nutrition','Psychology']
	for i in range(0,20):
		skill_dict[i] = skill_name[i]
	return skill_dict
	
def update_goals(new_goals):
	index = 0
	for goals in new_goals:
		c.execute("UPDATE goals SET value = '%d' WHERE uid = %d" %(goals,index));
		index = index + 1
	conn.commit();
	
def update_recommendation(skill_dict,ranked_skills):
	for index in range(0,6):
		c.execute("UPDATE skills_recommendation SET skill = '%s' WHERE uid = %d" %(skill_dict[ranked_skills[index][0]],index));
	conn.commit();
	
def update_job_col(job_ranking):
	index = 0
	for job_tuple in job_ranking:
		c.execute("UPDATE job_weight SET recommended_rank = '%f' WHERE uid= %d" %(index,job_tuple[0]));
		c.execute("UPDATE job_weight SET recommended_weight = '%f' WHERE uid= %d" %(job_tuple[1],job_tuple[0]));
		index = index + 1
	conn.commit();
	

#-------------------------------------------------------------------------

#Job Ranking algorithm----------------------------------------------------
def calculate_euclidian_distance(target,current):
	A = numpy.array(target)
	B = numpy.array(current)
	return scipy.spatial.distance.euclidean(A,B)
	
def rank_jobs(data):
	job_ranking = {}
	data_goals = []
	total = 0;
	for goal in data.goals:
		data_goals.append(float(goal.value));
	
	i = 0
	for job in data.jobs:
		job_ranking[i] = calculate_euclidian_distance(data_goals,job.goals)
		total = total + job_ranking[i]
		i += 1
	job_ranking = {key: total-value for key, value in job_ranking.iteritems()}	
	job_ranking = sorted(job_ranking.items(), key=lambda t: t[1])
	returning_job_rank = {}
	
	index = 0
	total = 0;
	for job_tuple in job_ranking:
		total += job_tuple[1];
	
	for job_tuple in job_ranking:
		returning_job_rank[job_tuple[0]]=(job_tuple[1]/total)
		index = index + 1
		
	returning_job_rank = sorted(returning_job_rank.items(), key=lambda t: t[1],reverse=True)
	return returning_job_rank
#-------------------------------------------------------------------------
	
#Skill Ranking Calculation
def calculate_skill_ranking(aggregated_skills,job_ranking,job_count,skill_count,data):
	cumulative_skills_score = {}
	for i in range(0,skill_count):
		cumulative_skills_score[i] = 0
		
	for i in range(0,job_count):
		for j in range(0,skill_count):
			cumulative_skills_score[j] += (job_ranking[i][1] -data.jobs[i].recommended_weight)*(aggregated_skills[i][j])
	
	cumulative_skills_score= {key: value for key, value in cumulative_skills_score.iteritems()}	
	cumulative_skills_score = sorted(cumulative_skills_score.items(), key=lambda t: t[1],reverse=True)
	return cumulative_skills_score
		

#Initialize the database
#initialize_db(populate_goals_value())

#Initialize the data and Simple euclidian distance
job_count = 6
goals_count = 5
data = Data(populate_jobs(job_count),populate_goals(goals_count))
update_goals([5,1,1,1,2])
job_ranking = rank_jobs(data)
index = 0
print("Goals inputed : Security = 5, Wealth = 1, Exploration = 1 , Innovation = 1, Expension = 2")

print("Job ranking :")
for job_tuple in job_ranking:
	print('Job : %s ranking is %d with new target = %f%%' %(data.jobs[job_tuple[0]].name,index,job_tuple[1]))
	index = index + 1
update_job_col(job_ranking);
	

#Skill selection:
skill_array = populate_skill_array()
skill_count = 20
ranked_skills = calculate_skill_ranking(skill_array,job_ranking,job_count,skill_count,data)

skill_dict = populate_skill_dict()
for i in range(0,skill_count):
	print("Skill : %s is ranked %d" %(skill_dict[ranked_skills[i][0]],i))
update_recommendation(skill_dict,ranked_skills)



#Show the plot with matplotlib
#ranked_skills and skill_dict, got the skill list ranked
#job_ranking is where my job are in ranked order

data = Data(populate_jobs(job_count),populate_goals(goals_count))
recommended_weight_plot = []
current_weight_plot = []
for i in range(0,6):
	recommended_weight_plot.append(data.jobs[i].recommended_weight);
	current_weight_plot.append(data.jobs[i].current_weight)
recommended_weight_plot = numpy.array(recommended_weight_plot)
current_weight_plot = numpy.array(current_weight_plot)


labels = ['test','Maintenance Worker','Lead Process Planner','Ressource Excavator','Medic','Harvester','Guardian']
data = [current_weight_plot,
  recommended_weight_plot]

f, (ax1, ax2) = plt.subplots(2, 1, sharey=True)
X = numpy.arange(6)
rects_1 = ax1.bar(X -0.125, data[0], color = 'g', width = 0.25,label='Current')
rects_2 = ax1.bar(X + 0.125, data[1], color = 'gold', width = 0.25,label='Recommended')
ax1.set_ylim([min(recommended_weight_plot)-0.002,max(recommended_weight_plot)+0.01])
ax1.set_xticklabels(labels)
ax1.set_title('Comparison of Actual and Recommended Job Partition')
ax1.legend(loc='upper left')

def autolabel(rects,data):
	index = 0
	for rect in rects:
		height = data[index]
		ax1.text(rect.get_x() + rect.get_width()/2., 1.01*height,
			'%.2f' % (height),
			ha='center', va='bottom')
		index += 1
					
autolabel(rects_1,data[0])
autolabel(rects_2,data[1])

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = []
labels.append('test')
for i in range(0,6):
	labels.append(skill_dict[ranked_skills[i][0]])
	
label_value = max(recommended_weight_plot)
data = [label_value, label_value, label_value, label_value, label_value,label_value]

ax2.bar(X, data[0], color = 'b', width = 0.25)
ax2.set_xticklabels(labels)
ax2.set_ylim([min(recommended_weight_plot)-0.002,max(recommended_weight_plot)+0.01])
ax2.set_title('Proposed Skills to Promote')
mng = plt.get_current_fig_manager()
mng.window.state('zoomed') #works fine on Windows!

plt.show()



conn.close()
