Rails.application.routes.draw do
  devise_for :users, :controllers => {:registrations => "registrations"}
  resources :jobs
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'welcome#index'
  get 'skills/:skill', to: 'jobs#index', as: :skill

  # more user friendly url
  devise_scope :user do
  get 'login', to: 'devise/sessions#new'
	end
	devise_scope :user do
		get 'signup', to: 'devise/registrations#new'
	end

end
