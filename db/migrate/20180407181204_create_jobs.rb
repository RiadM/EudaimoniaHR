class CreateJobs < ActiveRecord::Migration[5.1]
  def change
    create_table :jobs do |t|
      t.string :name
      t.integer :weight

      t.timestamps
    end
    add_index :jobs, :name, unique: true
  end
end
