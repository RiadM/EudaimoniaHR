class CreateTaggings < ActiveRecord::Migration[5.1]
  def change
    create_table :taggings do |t|
      t.belongs_to :skill, foreign_key: true
      t.belongs_to :job, foreign_key: true

      t.timestamps
    end
  end
end
