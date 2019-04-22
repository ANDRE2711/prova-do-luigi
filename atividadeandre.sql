if not exists(select * from INFORMATION_SCHEMA.tables where table_name = 'andreexpress') 
	begin
	create table andreexpress
	(
		id_andreexpress integer identity(1,1) constraint PK_id_alunos primary key,
		tipodemercadoria varchar(100),
		quantidade int ,
		cor varchar(10) null,
		preco int,
		descricao varchar(100) null
	)
	end
	go

	select * from andreexpress

	

	
