class JobsController < ApplicationController

  def index
    @jobs = if params[:skill]
      Job.tagged_with(params[:skill])
    else
      Job.all
    end
  end

  def new
    @job = Job.new
  end

  def show
    @job = Job.find(params[:id])
  end

  def create
    @job = Job.new(job_params)

    if @job.save
        redirect_to @job, notice: 'Job was successfully created.' 
      else
        render :new
    end
  end

  def edit
    @job = Job.find(params[:id])
  end

  def update
    @job = Job.find(params[:id])
    if @job.update_attributes(job_params)
      redirect_to @job, notice: 'The job has been updated.'
    else
      render :edit
    end
  end

  private
    def set_job
      @job = Job.find(params[:id])
    end

    def job_params
      params.require(:job).permit(:name, :weight, :skill_list)
    end
end
