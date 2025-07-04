import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os

class LaboratorioClinicoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Laboratorio Clínico")
        self.root.geometry("1200x700")
        
        # Variables para almacenar datos
        self.pacientes = []
        self.examenes = []
        self.medicos = []
        self.citas = []
        
        # Cargar datos existentes
        self.cargar_datos()
        
        # Crear pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        # Pestaña de Pacientes
        self.tab_pacientes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_pacientes, text="Pacientes")
        self.crear_interfaz_pacientes()
        
        # Pestaña de Médicos
        self.tab_medicos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_medicos, text="Médicos")
        self.crear_interfaz_medicos()
        
        # Pestaña de Exámenes
        self.tab_examenes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_examenes, text="Exámenes")
        self.crear_interfaz_examenes()
        
        # Pestaña de Citas
        self.tab_citas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_citas, text="Citas/Agenda")
        self.crear_interfaz_citas()
        
        # Pestaña de Reportes
        self.tab_reportes = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reportes, text="Reportes")
        self.crear_interfaz_reportes()
        
        # Configuración del laboratorio
        self.nombre_laboratorio = "Laboratorio Clínico Ejemplo"
        self.sello_laboratorio = "Sello Oficial LC-2023"
    
    def cargar_datos(self):
        # Cargar pacientes
        if os.path.exists('pacientes.csv'):
            with open('pacientes.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.pacientes = list(reader)
        
        # Cargar médicos
        if os.path.exists('medicos.csv'):
            with open('medicos.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.medicos = list(reader)
        
        # Cargar exámenes
        if os.path.exists('examenes.csv'):
            with open('examenes.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.examenes = list(reader)
        
        # Cargar citas
        if os.path.exists('citas.csv'):
            with open('citas.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.citas = list(reader)
    
    def guardar_datos(self):
        # Guardar pacientes
        with open('pacientes.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'cedula', 'nombre', 'apellido', 'fecha_nacimiento', 'celular']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.pacientes)
        
        # Guardar médicos
        with open('medicos.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'nombre', 'especialidad']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.medicos)
        
        # Guardar exámenes
        with open('examenes.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'nombre', 'tipo', 'descripcion']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.examenes)
        
        # Guardar citas
        with open('citas.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'id_paciente', 'id_medico', 'id_examen', 'fecha', 'hora', 'estado', 'resultados']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.citas)
    
    def crear_interfaz_pacientes(self):
        # Frame de entrada de datos
        frame_entrada = ttk.LabelFrame(self.tab_pacientes, text="Datos del Paciente")
        frame_entrada.pack(padx=10, pady=10, fill='x')
        
        # Campos del formulario
        ttk.Label(frame_entrada, text="Cédula:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.cedula_entry = ttk.Entry(frame_entrada)
        self.cedula_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.nombre_entry = ttk.Entry(frame_entrada)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Apellido:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.apellido_entry = ttk.Entry(frame_entrada)
        self.apellido_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Fecha Nacimiento (dd/mm/aaaa):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.fecha_nac_entry = ttk.Entry(frame_entrada)
        self.fecha_nac_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Celular:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.celular_entry = ttk.Entry(frame_entrada)
        self.celular_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        
        # Botones
        frame_botones = ttk.Frame(self.tab_pacientes)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_paciente).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Modificar", command=self.modificar_paciente).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_paciente).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_formulario_paciente).pack(side='left', padx=5)
        
        # Tabla de pacientes
        frame_tabla = ttk.Frame(self.tab_pacientes)
        frame_tabla.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.tree_pacientes = ttk.Treeview(frame_tabla, columns=('id', 'cedula', 'nombre', 'apellido', 'fecha_nac', 'celular'), show='headings')
        self.tree_pacientes.heading('id', text='ID')
        self.tree_pacientes.heading('cedula', text='Cédula')
        self.tree_pacientes.heading('nombre', text='Nombre')
        self.tree_pacientes.heading('apellido', text='Apellido')
        self.tree_pacientes.heading('fecha_nac', text='Fecha Nacimiento')
        self.tree_pacientes.heading('celular', text='Celular')
        
        self.tree_pacientes.column('id', width=50)
        self.tree_pacientes.column('cedula', width=100)
        self.tree_pacientes.column('nombre', width=150)
        self.tree_pacientes.column('apellido', width=150)
        self.tree_pacientes.column('fecha_nac', width=120)
        self.tree_pacientes.column('celular', width=100)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tree_pacientes.yview)
        self.tree_pacientes.configure(yscrollcommand=scrollbar.set)
        
        self.tree_pacientes.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.tree_pacientes.bind('<<TreeviewSelect>>', self.cargar_paciente_seleccionado)
        
        self.actualizar_tabla_pacientes()
    
    def crear_interfaz_medicos(self):
        # Frame de entrada de datos
        frame_entrada = ttk.LabelFrame(self.tab_medicos, text="Datos del Médico")
        frame_entrada.pack(padx=10, pady=10, fill='x')
        
        # Campos del formulario
        ttk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.medico_nombre_entry = ttk.Entry(frame_entrada)
        self.medico_nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Especialidad:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.especialidad_entry = ttk.Entry(frame_entrada)
        self.especialidad_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        # Botones
        frame_botones = ttk.Frame(self.tab_medicos)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_medico).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Modificar", command=self.modificar_medico).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_medico).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_formulario_medico).pack(side='left', padx=5)
        
        # Tabla de médicos
        frame_tabla = ttk.Frame(self.tab_medicos)
        frame_tabla.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.tree_medicos = ttk.Treeview(frame_tabla, columns=('id', 'nombre', 'especialidad'), show='headings')
        self.tree_medicos.heading('id', text='ID')
        self.tree_medicos.heading('nombre', text='Nombre')
        self.tree_medicos.heading('especialidad', text='Especialidad')
        
        self.tree_medicos.column('id', width=50)
        self.tree_medicos.column('nombre', width=200)
        self.tree_medicos.column('especialidad', width=200)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tree_medicos.yview)
        self.tree_medicos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_medicos.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.tree_medicos.bind('<<TreeviewSelect>>', self.cargar_medico_seleccionado)
        
        self.actualizar_tabla_medicos()
    
    def crear_interfaz_examenes(self):
        # Frame de entrada de datos
        frame_entrada = ttk.LabelFrame(self.tab_examenes, text="Datos del Examen")
        frame_entrada.pack(padx=10, pady=10, fill='x')
        
        # Campos del formulario
        ttk.Label(frame_entrada, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.examen_nombre_entry = ttk.Entry(frame_entrada)
        self.examen_nombre_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Tipo:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.examen_tipo_entry = ttk.Entry(frame_entrada)
        self.examen_tipo_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.examen_desc_entry = ttk.Entry(frame_entrada)
        self.examen_desc_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        # Botones
        frame_botones = ttk.Frame(self.tab_examenes)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_examen).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Modificar", command=self.modificar_examen).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_examen).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_formulario_examen).pack(side='left', padx=5)
        
        # Tabla de exámenes
        frame_tabla = ttk.Frame(self.tab_examenes)
        frame_tabla.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.tree_examenes = ttk.Treeview(frame_tabla, columns=('id', 'nombre', 'tipo', 'descripcion'), show='headings')
        self.tree_examenes.heading('id', text='ID')
        self.tree_examenes.heading('nombre', text='Nombre')
        self.tree_examenes.heading('tipo', text='Tipo')
        self.tree_examenes.heading('descripcion', text='Descripción')
        
        self.tree_examenes.column('id', width=50)
        self.tree_examenes.column('nombre', width=150)
        self.tree_examenes.column('tipo', width=150)
        self.tree_examenes.column('descripcion', width=300)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tree_examenes.yview)
        self.tree_examenes.configure(yscrollcommand=scrollbar.set)
        
        self.tree_examenes.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.tree_examenes.bind('<<TreeviewSelect>>', self.cargar_examen_seleccionado)
        
        self.actualizar_tabla_examenes()
    
    def crear_interfaz_citas(self):
        # Frame de entrada de datos
        frame_entrada = ttk.LabelFrame(self.tab_citas, text="Agendar Cita")
        frame_entrada.pack(padx=10, pady=10, fill='x')
        
        # Campos del formulario
        ttk.Label(frame_entrada, text="Paciente:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.cita_paciente_combo = ttk.Combobox(frame_entrada, state='readonly')
        self.cita_paciente_combo.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Médico:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.cita_medico_combo = ttk.Combobox(frame_entrada, state='readonly')
        self.cita_medico_combo.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Examen:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.cita_examen_combo = ttk.Combobox(frame_entrada, state='readonly')
        self.cita_examen_combo.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.cita_fecha_entry = ttk.Entry(frame_entrada)
        self.cita_fecha_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Label(frame_entrada, text="Hora:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.cita_hora_entry = ttk.Entry(frame_entrada)
        self.cita_hora_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        
        # Botones
        frame_botones = ttk.Frame(self.tab_citas)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Agendar", command=self.agendar_cita).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Cancelar", command=self.cancelar_cita).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Completar", command=self.completar_cita).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self.limpiar_formulario_cita).pack(side='left', padx=5)
        
        # Tabla de citas
        frame_tabla = ttk.Frame(self.tab_citas)
        frame_tabla.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.tree_citas = ttk.Treeview(frame_tabla, columns=('id', 'paciente', 'medico', 'examen', 'fecha', 'hora', 'estado'), show='headings')
        self.tree_citas.heading('id', text='ID')
        self.tree_citas.heading('paciente', text='Paciente')
        self.tree_citas.heading('medico', text='Médico')
        self.tree_citas.heading('examen', text='Examen')
        self.tree_citas.heading('fecha', text='Fecha')
        self.tree_citas.heading('hora', text='Hora')
        self.tree_citas.heading('estado', text='Estado')
        
        self.tree_citas.column('id', width=50)
        self.tree_citas.column('paciente', width=150)
        self.tree_citas.column('medico', width=150)
        self.tree_citas.column('examen', width=150)
        self.tree_citas.column('fecha', width=100)
        self.tree_citas.column('hora', width=80)
        self.tree_citas.column('estado', width=100)
        
        scrollbar = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tree_citas.yview)
        self.tree_citas.configure(yscrollcommand=scrollbar.set)
        
        self.tree_citas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.tree_citas.bind('<<TreeviewSelect>>', self.cargar_cita_seleccionada)
        
        self.actualizar_tabla_citas()
        self.actualizar_comboboxes_citas()
    
    def crear_interfaz_reportes(self):
        # Frame de filtros
        frame_filtros = ttk.LabelFrame(self.tab_reportes, text="Filtros")
        frame_filtros.pack(padx=10, pady=10, fill='x')
        
        ttk.Label(frame_filtros, text="Fecha inicial:").grid(row=0, column=0, padx=5, pady=5)
        self.reporte_fecha_inicio = ttk.Entry(frame_filtros)
        self.reporte_fecha_inicio.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_filtros, text="Fecha final:").grid(row=0, column=2, padx=5, pady=5)
        self.reporte_fecha_fin = ttk.Entry(frame_filtros)
        self.reporte_fecha_fin.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(frame_filtros, text="Tipo de examen:").grid(row=1, column=0, padx=5, pady=5)
        self.reporte_tipo_examen = ttk.Combobox(frame_filtros, state='readonly')
        self.reporte_tipo_examen.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_filtros, text="Médico:").grid(row=1, column=2, padx=5, pady=5)
        self.reporte_medico = ttk.Combobox(frame_filtros, state='readonly')
        self.reporte_medico.grid(row=1, column=3, padx=5, pady=5)
        
        # Botones
        frame_botones = ttk.Frame(self.tab_reportes)
        frame_botones.pack(pady=10)
        
        ttk.Button(frame_botones, text="Generar Reporte", command=self.generar_reporte).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Exportar a PDF", command=self.exportar_a_pdf).pack(side='left', padx=5)
        
        # Área de resultados
        frame_resultados = ttk.Frame(self.tab_reportes)
        frame_resultados.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.text_reporte = tk.Text(frame_resultados, wrap='word')
        scrollbar = ttk.Scrollbar(frame_resultados, orient='vertical', command=self.text_reporte.yview)
        self.text_reporte.configure(yscrollcommand=scrollbar.set)
        
        self.text_reporte.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Configurar comboboxes
        tipos_examen = list(set(examen['tipo'] for examen in self.examenes))
        self.reporte_tipo_examen['values'] = ['Todos'] + tipos_examen
        self.reporte_tipo_examen.set('Todos')
        
        nombres_medicos = [medico['nombre'] for medico in self.medicos]
        self.reporte_medico['values'] = ['Todos'] + nombres_medicos
        self.reporte_medico.set('Todos')
    
    # Métodos para pacientes
    def agregar_paciente(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        fecha_nac = self.fecha_nac_entry.get()
        celular = self.celular_entry.get()
        
        if not all([cedula, nombre, apellido, fecha_nac, celular]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        nuevo_id = str(max([int(p['id']) for p in self.pacientes] + [0]) + 1)
        
        paciente = {
            'id': nuevo_id,
            'cedula': cedula,
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nac,
            'celular': celular
        }
        
        self.pacientes.append(paciente)
        self.guardar_datos()
        self.actualizar_tabla_pacientes()
        self.limpiar_formulario_paciente()
        messagebox.showinfo("Éxito", "Paciente agregado correctamente")
    
    def modificar_paciente(self):
        seleccionado = self.tree_pacientes.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un paciente para modificar")
            return
        
        item = self.tree_pacientes.item(seleccionado)
        paciente_id = item['values'][0]
        
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        fecha_nac = self.fecha_nac_entry.get()
        celular = self.celular_entry.get()
        
        if not all([cedula, nombre, apellido, fecha_nac, celular]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        for paciente in self.pacientes:
            if paciente['id'] == paciente_id:
                paciente['cedula'] = cedula
                paciente['nombre'] = nombre
                paciente['apellido'] = apellido
                paciente['fecha_nacimiento'] = fecha_nac
                paciente['celular'] = celular
                break
        
        self.guardar_datos()
        self.actualizar_tabla_pacientes()
        messagebox.showinfo("Éxito", "Paciente modificado correctamente")
    
    def eliminar_paciente(self):
        seleccionado = self.tree_pacientes.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un paciente para eliminar")
            return
        
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este paciente?")
        if not confirmacion:
            return
        
        item = self.tree_pacientes.item(seleccionado)
        paciente_id = item['values'][0]
        
        self.pacientes = [p for p in self.pacientes if p['id'] != paciente_id]
        self.guardar_datos()
        self.actualizar_tabla_pacientes()
        self.limpiar_formulario_paciente()
        messagebox.showinfo("Éxito", "Paciente eliminado correctamente")
    
    def cargar_paciente_seleccionado(self, event):
        seleccionado = self.tree_pacientes.selection()
        if not seleccionado:
            return
        
        item = self.tree_pacientes.item(seleccionado)
        valores = item['values']
        
        self.cedula_entry.delete(0, tk.END)
        self.cedula_entry.insert(0, valores[1])
        
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, valores[2])
        
        self.apellido_entry.delete(0, tk.END)
        self.apellido_entry.insert(0, valores[3])
        
        self.fecha_nac_entry.delete(0, tk.END)
        self.fecha_nac_entry.insert(0, valores[4])
        
        self.celular_entry.delete(0, tk.END)
        self.celular_entry.insert(0, valores[5])
    
    def limpiar_formulario_paciente(self):
        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.fecha_nac_entry.delete(0, tk.END)
        self.celular_entry.delete(0, tk.END)
    
    def actualizar_tabla_pacientes(self):
        for item in self.tree_pacientes.get_children():
            self.tree_pacientes.delete(item)
        
        for paciente in self.pacientes:
            self.tree_pacientes.insert('', 'end', values=(
                paciente['id'],
                paciente['cedula'],
                paciente['nombre'],
                paciente['apellido'],
                paciente['fecha_nacimiento'],
                paciente['celular']
            ))
    
    # Métodos para médicos (similar a pacientes)
    def agregar_medico(self):
        nombre = self.medico_nombre_entry.get()
        especialidad = self.especialidad_entry.get()
        
        if not all([nombre, especialidad]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        nuevo_id = str(max([int(m['id']) for m in self.medicos] + [0]) + 1)
        
        medico = {
            'id': nuevo_id,
            'nombre': nombre,
            'especialidad': especialidad
        }
        
        self.medicos.append(medico)
        self.guardar_datos()
        self.actualizar_tabla_medicos()
        self.limpiar_formulario_medico()
        messagebox.showinfo("Éxito", "Médico agregado correctamente")
        self.actualizar_comboboxes_citas()
    
    def modificar_medico(self):
        seleccionado = self.tree_medicos.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un médico para modificar")
            return
        
        item = self.tree_medicos.item(seleccionado)
        medico_id = item['values'][0]
        
        nombre = self.medico_nombre_entry.get()
        especialidad = self.especialidad_entry.get()
        
        if not all([nombre, especialidad]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        for medico in self.medicos:
            if medico['id'] == medico_id:
                medico['nombre'] = nombre
                medico['especialidad'] = especialidad
                break
        
        self.guardar_datos()
        self.actualizar_tabla_medicos()
        messagebox.showinfo("Éxito", "Médico modificado correctamente")
        self.actualizar_comboboxes_citas()
    
    def eliminar_medico(self):
        seleccionado = self.tree_medicos.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un médico para eliminar")
            return
        
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este médico?")
        if not confirmacion:
            return
        
        item = self.tree_medicos.item(seleccionado)
        medico_id = item['values'][0]
        
        # Verificar si el médico tiene citas asociadas
        citas_medico = [c for c in self.citas if c['id_medico'] == medico_id]
        if citas_medico:
            messagebox.showerror("Error", "No se puede eliminar, el médico tiene citas asociadas")
            return
        
        self.medicos = [m for m in self.medicos if m['id'] != medico_id]
        self.guardar_datos()
        self.actualizar_tabla_medicos()
        self.limpiar_formulario_medico()
        messagebox.showinfo("Éxito", "Médico eliminado correctamente")
        self.actualizar_comboboxes_citas()
    
    def cargar_medico_seleccionado(self, event):
        seleccionado = self.tree_medicos.selection()
        if not seleccionado:
            return
        
        item = self.tree_medicos.item(seleccionado)
        valores = item['values']
        
        self.medico_nombre_entry.delete(0, tk.END)
        self.medico_nombre_entry.insert(0, valores[1])
        
        self.especialidad_entry.delete(0, tk.END)
        self.especialidad_entry.insert(0, valores[2])
    
    def limpiar_formulario_medico(self):
        self.medico_nombre_entry.delete(0, tk.END)
        self.especialidad_entry.delete(0, tk.END)
    
    def actualizar_tabla_medicos(self):
        for item in self.tree_medicos.get_children():
            self.tree_medicos.delete(item)
        
        for medico in self.medicos:
            self.tree_medicos.insert('', 'end', values=(
                medico['id'],
                medico['nombre'],
                medico['especialidad']
            ))
    
    # Métodos para exámenes (similar a pacientes y médicos)
    def agregar_examen(self):
        nombre = self.examen_nombre_entry.get()
        tipo = self.examen_tipo_entry.get()
        descripcion = self.examen_desc_entry.get()
        
        if not all([nombre, tipo]):
            messagebox.showerror("Error", "Nombre y tipo son obligatorios")
            return
        
        nuevo_id = str(max([int(e['id']) for e in self.examenes] + [0]) + 1)
        
        examen = {
            'id': nuevo_id,
            'nombre': nombre,
            'tipo': tipo,
            'descripcion': descripcion
        }
        
        self.examenes.append(examen)
        self.guardar_datos()
        self.actualizar_tabla_examenes()
        self.limpiar_formulario_examen()
        messagebox.showinfo("Éxito", "Examen agregado correctamente")
        self.actualizar_comboboxes_citas()
    
    def modificar_examen(self):
        seleccionado = self.tree_examenes.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un examen para modificar")
            return
        
        item = self.tree_examenes.item(seleccionado)
        examen_id = item['values'][0]
        
        nombre = self.examen_nombre_entry.get()
        tipo = self.examen_tipo_entry.get()
        descripcion = self.examen_desc_entry.get()
        
        if not all([nombre, tipo]):
            messagebox.showerror("Error", "Nombre y tipo son obligatorios")
            return
        
        for examen in self.examenes:
            if examen['id'] == examen_id:
                examen['nombre'] = nombre
                examen['tipo'] = tipo
                examen['descripcion'] = descripcion
                break
        
        self.guardar_datos()
        self.actualizar_tabla_examenes()
        messagebox.showinfo("Éxito", "Examen modificado correctamente")
        self.actualizar_comboboxes_citas()
    
    def eliminar_examen(self):
        seleccionado = self.tree_examenes.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un examen para eliminar")
            return
        
        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este examen?")
        if not confirmacion:
            return
        
        item = self.tree_examenes.item(seleccionado)
        examen_id = item['values'][0]
        
        # Verificar si el examen tiene citas asociadas
        citas_examen = [c for c in self.citas if c['id_examen'] == examen_id]
        if citas_examen:
            messagebox.showerror("Error", "No se puede eliminar, el examen tiene citas asociadas")
            return
        
        self.examenes = [e for e in self.examenes if e['id'] != examen_id]
        self.guardar_datos()
        self.actualizar_tabla_examenes()
        self.limpiar_formulario_examen()
        messagebox.showinfo("Éxito", "Examen eliminado correctamente")
        self.actualizar_comboboxes_citas()
    
    def cargar_examen_seleccionado(self, event):
        seleccionado = self.tree_examenes.selection()
        if not seleccionado:
            return
        
        item = self.tree_examenes.item(seleccionado)
        valores = item['values']
        
        self.examen_nombre_entry.delete(0, tk.END)
        self.examen_nombre_entry.insert(0, valores[1])
        
        self.examen_tipo_entry.delete(0, tk.END)
        self.examen_tipo_entry.insert(0, valores[2])
        
        self.examen_desc_entry.delete(0, tk.END)
        self.examen_desc_entry.insert(0, valores[3])
    
    def limpiar_formulario_examen(self):
        self.examen_nombre_entry.delete(0, tk.END)
        self.examen_tipo_entry.delete(0, tk.END)
        self.examen_desc_entry.delete(0, tk.END)
    
    def actualizar_tabla_examenes(self):
        for item in self.tree_examenes.get_children():
            self.tree_examenes.delete(item)
        
        for examen in self.examenes:
            self.tree_examenes.insert('', 'end', values=(
                examen['id'],
                examen['nombre'],
                examen['tipo'],
                examen['descripcion']
            ))
    
    # Métodos para citas
    def agendar_cita(self):
        paciente_id = self.cita_paciente_combo.get().split(' - ')[0]
        medico_id = self.cita_medico_combo.get().split(' - ')[0]
        examen_id = self.cita_examen_combo.get().split(' - ')[0]
        fecha = self.cita_fecha_entry.get()
        hora = self.cita_hora_entry.get()
        
        if not all([paciente_id, medico_id, examen_id, fecha, hora]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Validar formato de fecha
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto (dd/mm/aaaa)")
            return
        
        # Validar formato de hora
        try:
            datetime.strptime(hora, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Formato de hora incorrecto (HH:MM)")
            return
        
        nuevo_id = str(max([int(c['id']) for c in self.citas] + [0]) + 1)
        
        cita = {
            'id': nuevo_id,
            'id_paciente': paciente_id,
            'id_medico': medico_id,
            'id_examen': examen_id,
            'fecha': fecha,
            'hora': hora,
            'estado': 'Agendada',
            'resultados': ''
        }
        
        self.citas.append(cita)
        self.guardar_datos()
        self.actualizar_tabla_citas()
        self.limpiar_formulario_cita()
        messagebox.showinfo("Éxito", "Cita agendada correctamente")
    
    def cancelar_cita(self):
        seleccionado = self.tree_citas.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione una cita para cancelar")
            return
        
        item = self.tree_citas.item(seleccionado)
        cita_id = item['values'][0]
        
        for cita in self.citas:
            if cita['id'] == cita_id:
                if cita['estado'] == 'Completada':
                    messagebox.showerror("Error", "No se puede cancelar una cita completada")
                    return
                cita['estado'] = 'Cancelada'
                break
        
        self.guardar_datos()
        self.actualizar_tabla_citas()
        messagebox.showinfo("Éxito", "Cita cancelada correctamente")
    
    def completar_cita(self):
        seleccionado = self.tree_citas.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione una cita para completar")
            return
        
        item = self.tree_citas.item(seleccionado)
        cita_id = item['values'][0]
        
        for cita in self.citas:
            if cita['id'] == cita_id:
                if cita['estado'] == 'Cancelada':
                    messagebox.showerror("Error", "No se puede completar una cita cancelada")
                    return
                
                # Ventana para ingresar resultados
                top = tk.Toplevel(self.root)
                top.title("Ingresar Resultados")
                top.geometry("600x400")
                
                ttk.Label(top, text="Resultados del examen:").pack(pady=10)
                
                resultados_text = tk.Text(top, wrap='word')
                scrollbar = ttk.Scrollbar(top, orient='vertical', command=resultados_text.yview)
                resultados_text.configure(yscrollcommand=scrollbar.set)
                
                resultados_text.pack(side='left', fill='both', expand=True, padx=10, pady=10)
                scrollbar.pack(side='right', fill='y')
                
                # Mostrar información de la cita
                info_frame = ttk.Frame(top)
                info_frame.pack(fill='x', padx=10, pady=5)
                
                paciente_nombre = next((p['nombre'] + ' ' + p['apellido'] for p in self.pacientes if p['id'] == cita['id_paciente']), '')
                medico_nombre = next((m['nombre'] for m in self.medicos if m['id'] == cita['id_medico']), '')
                examen_nombre = next((e['nombre'] for e in self.examenes if e['id'] == cita['id_examen']), '')
                
                ttk.Label(info_frame, text=f"Paciente: {paciente_nombre}").pack(anchor='w')
                ttk.Label(info_frame, text=f"Médico: {medico_nombre}").pack(anchor='w')
                ttk.Label(info_frame, text=f"Examen: {examen_nombre}").pack(anchor='w')
                ttk.Label(info_frame, text=f"Fecha: {cita['fecha']} {cita['hora']}").pack(anchor='w')
                
                def guardar_resultados():
                    cita['resultados'] = resultados_text.get("1.0", tk.END).strip()
                    cita['estado'] = 'Completada'
                    self.guardar_datos()
                    self.actualizar_tabla_citas()
                    top.destroy()
                    messagebox.showinfo("Éxito", "Resultados guardados y cita completada")
                
                ttk.Button(top, text="Guardar Resultados", command=guardar_resultados).pack(pady=10)
                
                return
    
    def cargar_cita_seleccionada(self, event):
        seleccionado = self.tree_citas.selection()
        if not seleccionado:
            return
        
        item = self.tree_citas.item(seleccionado)
        cita_id = item['values'][0]
        
        cita = next((c for c in self.citas if c['id'] == cita_id), None)
        if not cita:
            return
        
        # Buscar los textos completos para mostrar en los comboboxes
        paciente_text = next((f"{p['id']} - {p['nombre']} {p['apellido']}" for p in self.pacientes if p['id'] == cita['id_paciente']), '')
        medico_text = next((f"{m['id']} - {m['nombre']}" for m in self.medicos if m['id'] == cita['id_medico']), '')
        examen_text = next((f"{e['id']} - {e['nombre']}" for e in self.examenes if e['id'] == cita['id_examen']), '')
        
        self.cita_paciente_combo.set(paciente_text)
        self.cita_medico_combo.set(medico_text)
        self.cita_examen_combo.set(examen_text)
        self.cita_fecha_entry.delete(0, tk.END)
        self.cita_fecha_entry.insert(0, cita['fecha'])
        self.cita_hora_entry.delete(0, tk.END)
        self.cita_hora_entry.insert(0, cita['hora'])
    
    def limpiar_formulario_cita(self):
        self.cita_paciente_combo.set('')
        self.cita_medico_combo.set('')
        self.cita_examen_combo.set('')
        self.cita_fecha_entry.delete(0, tk.END)
        self.cita_hora_entry.delete(0, tk.END)
    
    def actualizar_tabla_citas(self):
        for item in self.tree_citas.get_children():
            self.tree_citas.delete(item)
        
        for cita in self.citas:
            paciente_nombre = next((p['nombre'] + ' ' + p['apellido'] for p in self.pacientes if p['id'] == cita['id_paciente']), 'Desconocido')
            medico_nombre = next((m['nombre'] for m in self.medicos if m['id'] == cita['id_medico']), 'Desconocido')
            examen_nombre = next((e['nombre'] for e in self.examenes if e['id'] == cita['id_examen']), 'Desconocido')
            
            self.tree_citas.insert('', 'end', values=(
                cita['id'],
                paciente_nombre,
                medico_nombre,
                examen_nombre,
                cita['fecha'],
                cita['hora'],
                cita['estado']
            ))
    
    def actualizar_comboboxes_citas(self):
        # Actualizar combobox de pacientes
        pacientes_text = [f"{p['id']} - {p['nombre']} {p['apellido']}" for p in self.pacientes]
        self.cita_paciente_combo['values'] = pacientes_text
        
        # Actualizar combobox de médicos
        medicos_text = [f"{m['id']} - {m['nombre']}" for m in self.medicos]
        self.cita_medico_combo['values'] = medicos_text
        
        # Actualizar combobox de exámenes
        examenes_text = [f"{e['id']} - {e['nombre']}" for e in self.examenes]
        self.cita_examen_combo['values'] = examenes_text
    
    # Métodos para reportes
    def generar_reporte(self):
        fecha_inicio = self.reporte_fecha_inicio.get()
        fecha_fin = self.reporte_fecha_fin.get()
        tipo_examen = self.reporte_tipo_examen.get()
        medico = self.reporte_medico.get()
        
        # Validar fechas
        try:
            if fecha_inicio:
                fecha_inicio_dt = datetime.strptime(fecha_inicio, '%d/%m/%Y')
            if fecha_fin:
                fecha_fin_dt = datetime.strptime(fecha_fin, '%d/%m/%Y')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto (dd/mm/aaaa)")
            return
        
        # Filtrar citas
        citas_filtradas = []
        for cita in self.citas:
            # Filtrar por estado (solo completadas)
            if cita['estado'] != 'Completada':
                continue
            
            # Filtrar por fecha
            cita_fecha = datetime.strptime(cita['fecha'], '%d/%m/%Y')
            if fecha_inicio and cita_fecha < fecha_inicio_dt:
                continue
            if fecha_fin and cita_fecha > fecha_fin_dt:
                continue
            
            # Filtrar por tipo de examen
            examen = next((e for e in self.examenes if e['id'] == cita['id_examen']), None)
            if tipo_examen != 'Todos' and examen and examen['tipo'] != tipo_examen:
                continue
            
            # Filtrar por médico
            medico_nombre = next((m['nombre'] for m in self.medicos if m['id'] == cita['id_medico']), '')
            if medico != 'Todos' and medico_nombre != medico:
                continue
            
            citas_filtradas.append(cita)
        
        # Generar reporte
        self.text_reporte.delete('1.0', tk.END)
        
        # Encabezado del reporte
        self.text_reporte.insert(tk.END, f"{self.nombre_laboratorio}\n", 'titulo')
        self.text_reporte.insert(tk.END, f"Reporte de Exámenes Clínicos\n\n", 'subtitulo')
        
        # Filtros aplicados
        self.text_reporte.insert(tk.END, "Filtros aplicados:\n", 'encabezado')
        self.text_reporte.insert(tk.END, f"Fecha inicial: {fecha_inicio if fecha_inicio else 'No especificada'}\n")
        self.text_reporte.insert(tk.END, f"Fecha final: {fecha_fin if fecha_fin else 'No especificada'}\n")
        self.text_reporte.insert(tk.END, f"Tipo de examen: {tipo_examen}\n")
        self.text_reporte.insert(tk.END, f"Médico: {medico}\n\n")
        
        # Resumen estadístico
        total_examenes = len(citas_filtradas)
        tipos_examen = {}
        medicos = {}
        
        for cita in citas_filtradas:
            examen = next((e for e in self.examenes if e['id'] == cita['id_examen']), None)
            if examen:
                tipos_examen[examen['tipo']] = tipos_examen.get(examen['tipo'], 0) + 1
            
            medico_nombre = next((m['nombre'] for m in self.medicos if m['id'] == cita['id_medico']), 'Desconocido')
            medicos[medico_nombre] = medicos.get(medico_nombre, 0) + 1
        
        self.text_reporte.insert(tk.END, f"Total de exámenes: {total_examenes}\n\n", 'encabezado')
        
        self.text_reporte.insert(tk.END, "Distribución por tipo de examen:\n", 'encabezado')
        for tipo, cantidad in tipos_examen.items():
            self.text_reporte.insert(tk.END, f"- {tipo}: {cantidad}\n")
        
        self.text_reporte.insert(tk.END, "\nDistribución por médico:\n", 'encabezado')
        for medico_nombre, cantidad in medicos.items():
            self.text_reporte.insert(tk.END, f"- {medico_nombre}: {cantidad}\n")
        
        # Detalle de exámenes
        self.text_reporte.insert(tk.END, "\nDetalle de exámenes:\n", 'encabezado')
        for cita in citas_filtradas:
            paciente = next((p for p in self.pacientes if p['id'] == cita['id_paciente']), None)
            medico = next((m for m in self.medicos if m['id'] == cita['id_medico']), None)
            examen = next((e for e in self.examenes if e['id'] == cita['id_examen']), None)
            
            if paciente and medico and examen:
                self.text_reporte.insert(tk.END, "\n" + "="*50 + "\n", 'separador')
                self.text_reporte.insert(tk.END, f"Fecha: {cita['fecha']} {cita['hora']}\n")
                self.text_reporte.insert(tk.END, f"Paciente: {paciente['nombre']} {paciente['apellido']} (Cédula: {paciente['cedula']})\n")
                self.text_reporte.insert(tk.END, f"Médico: {medico['nombre']} - {medico['especialidad']}\n")
                self.text_reporte.insert(tk.END, f"Examen: {examen['nombre']} ({examen['tipo']})\n")
                self.text_reporte.insert(tk.END, f"Resultados:\n{cita['resultados']}\n")
        
        # Pie de página
        self.text_reporte.insert(tk.END, "\n" + "="*50 + "\n", 'separador')
        self.text_reporte.insert(tk.END, f"Reporte generado el: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        self.text_reporte.insert(tk.END, f"Sello: {self.sello_laboratorio}\n", 'sello')
    
    def exportar_a_pdf(self):
        # Esta función requeriría la instalación de una librería como reportlab o fpdf
        # Aquí se muestra un esqueleto de cómo podría implementarse
        messagebox.showinfo("Información", "Esta función exportaría el reporte a PDF. Requiere librerías adicionales.")
        # from fpdf import FPDF
        # pdf = FPDF()
        # pdf.add_page()
        # pdf.set_font("Arial", size=12)
        # pdf.cell(200, 10, txt="Reporte del Laboratorio", ln=1, align='C')
        # ... más código para generar el PDF ...
        # pdf.output("reporte_laboratorio.pdf")

# Configurar estilos
def configurar_estilos():
    style = ttk.Style()
    style.configure('TButton', padding=6, relief='flat', background='#ccc')
    style.configure('TLabel', padding=6, background='#f0f0f0')
    style.configure('TEntry', padding=6)
    style.configure('TFrame', background='#f0f0f0')
    style.configure('Treeview', rowheight=25)
    style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

# Función principal
def main():
    root = tk.Tk()
    configurar_estilos()
    app = LaboratorioClinicoApp(root)
    
    # Configurar etiquetas de texto
    root.option_add('*Text.background', 'white')
    root.option_add('*Text.font', 'Arial 10')
    root.option_add('*Text.tag.titulo.font', 'Arial 14 bold')
    root.option_add('*Text.tag.subtitulo.font', 'Arial 12 bold')
    root.option_add('*Text.tag.encabezado.font', 'Arial 10 bold')
    root.option_add('*Text.tag.sello.font', 'Arial 8 italic')
    root.option_add('*Text.tag.separador.foreground', 'gray')
    
    root.mainloop()

if _name_ == "_main_":
    main()