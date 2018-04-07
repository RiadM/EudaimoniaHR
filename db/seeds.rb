# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'faker'

skills_array = ['Savoir', 'Courage', 'Creativity', 'Force']

(1..10).each do |i|
	skills = []
	(0..3).each do |j|
		if rand(0..1) == 1
			skills << skills_array[j]
		end
	end

	job = Job.create(name: Faker::Job.unique.title, weight: rand(0..10), skill_list: skills.join(", "))
end

