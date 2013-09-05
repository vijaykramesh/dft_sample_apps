require 'sinatra'

get '/hello' do
  "Hello #{params[:name]}"
end
