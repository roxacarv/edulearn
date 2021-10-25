def contar_alunos_com_deficiencia(row):
  #Quantidade de alunos deficientes em cada curso
  return len(df_aluno.loc[df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']].index)
df_curso['ALUNOS_COM_DEFICIENCIA'] = df_curso.apply(contar_alunos_com_deficiencia, axis=1)

def contar_alunos_com_deficiencia_auditiva(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_AUDITIVA'] == 1)].index)
df_curso['ALUNOS_COM_DEFICIENCIA_AUDITIVA'] = df_curso.apply(contar_alunos_com_deficiencia_auditiva, axis=1)

def contar_alunos_com_deficiencia_fisica(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_FISICA'] == 1)].index)
df_curso['ALUNOS_COM_DEFICIENCIA_FISICA'] = df_curso.apply(contar_alunos_com_deficiencia_fisica, axis=1)

def contar_alunos_com_deficiencia_intelectual(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_INTELECTUAL'] == 1)].index)
df_curso['ALUNOS_COM_DEFICIENCIA_INTELECTUAL'] = df_curso.apply(contar_alunos_com_deficiencia_intelectual, axis=1)

def contar_alunos_com_deficiencia_multipla(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_MULTIPLA'] == 1)].index)
df_curso['ALUNOS_COM_DEFICIENCIA_MULTIPLA'] = df_curso.apply(contar_alunos_com_deficiencia_multipla, axis=1)

def contar_alunos_com_surdez(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_SURDEZ'] == 1)].index)
df_curso['ALUNOS_COM_SURDEZ'] = df_curso.apply(contar_alunos_com_surdez, axis=1)

def contar_alunos_com_surdocegueira(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_SURDOCEGUEIRA'] == 1)].index)
df_curso['ALUNOS_COM_SURDOCEGUEIRA'] = df_curso.apply(contar_alunos_com_surdocegueira, axis=1)

def contar_alunos_com_baixa_visao(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_BAIXA_VISAO'] == 1)].index)
df_curso['ALUNOS_COM_BAIXA_VISAO'] = df_curso.apply(contar_alunos_com_baixa_visao, axis=1)

def contar_alunos_com_cegueira(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_CEGUEIRA'] == 1)].index)
df_curso['ALUNOS_COM_CEGUEIRA'] = df_curso.apply(contar_alunos_com_cegueira, axis=1)

def contar_alunos_com_superdotacao(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_DEFICIENCIA_SUPERDOTACAO'] == 1)].index)
df_curso['ALUNOS_COM_SUPERDOTACAO'] = df_curso.apply(contar_alunos_com_superdotacao, axis=1)

def contar_alunos_com_autismo(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_TGD_AUTISMO'] == 1)].index)
df_curso['ALUNOS_COM_TGD_AUTISMO'] = df_curso.apply(contar_alunos_com_autismo, axis=1)

def contar_alunos_com_sindrome_asperger(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_TGD_SINDROME_ASPERGER'] == 1)].index)
df_curso['ALUNOS_COM_TGD_SINDROME_ASPERGER'] = df_curso.apply(contar_alunos_com_sindrome_asperger, axis=1)

def contar_alunos_com_sindrome_rett(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_TGD_SINDROME_RETT'] == 1)].index)
df_curso['ALUNOS_COM_TGD_SINDROME_RETT'] = df_curso.apply(contar_alunos_com_sindrome_rett, axis=1)

def contar_alunos_com_tgd_transtor_desintegrativo(row):
  #Quantidade de alunos com deficiência auditiva em cada curso
  return len(df_aluno.loc[(df_aluno['CODIGO_CURSO'] == row['CODIGO_CURSO']) & (df_aluno['IN_TGD_TRANSTOR_DESINTEGRATIVO'] == 1)].index)
df_curso['ALUNOS_COM_TGD_TRANSTOR_DESINTEGRATIVO'] = df_curso.apply(contar_alunos_com_tgd_transtor_desintegrativo, axis=1)

df_curso.head()