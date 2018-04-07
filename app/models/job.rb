class Job < ApplicationRecord
	has_many :taggings
	has_many :skills, through: :taggings

	def self.tagged_with(name)
		Skill.find_by!(name: name).jobs
	end

	def self.skill_counts
		Skill.select('skills.*, count(taggings.skill_id) as count').joins(:taggings).group('taggings.skill_id')
	end

	def skill_list
		skills.map(&:name).join(', ')
	end

	def skill_list=(names)
		self.skills = names.split(',').map do |i|
			Skill.where(name: i.strip).first_or_create!
		end
	end	
end
