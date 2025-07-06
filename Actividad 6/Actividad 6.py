from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox


# ---------------------------------------------------------------------
# 1.  MODELO
# ---------------------------------------------------------------------
@dataclass
class Student:
    student_id: str
    name: str
    age: int
    email: str

    @staticmethod
    def from_line(line: str) -> "Student":
        """Crea un Student a partir de una línea ID|Nombre|Edad|Correo"""
        parts = line.strip().split("|")
        if len(parts) != 4:
            raise ValueError("Línea mal formada en students.txt")
        sid, name, age, email = parts
        return Student(student_id=sid, name=name, age=int(age), email=email)

    def to_line(self) -> str:
        """Convierte el objeto a la representación de línea."""
        return f"{self.student_id}|{self.name}|{self.age}|{self.email}\n"


# ---------------------------------------------------------------------
# 2.  CAPA DE PERSISTENCIA (TXT)
# ---------------------------------------------------------------------
class StudentRepository:
    _data_file: Path = Path("students.txt")

    def __init__(self) -> None:
        # Crea el archivo si no existe
        self._data_file.touch(exist_ok=True)

    # -------- utilidades internas ------------------------------------
    def _read_all(self) -> list[Student]:
        students: list[Student] = []
        with self._data_file.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                students.append(Student.from_line(line))
        return students

    def _write_all(self, students: list[Student]) -> None:
        with self._data_file.open("w", encoding="utf-8") as f:
            for s in students:
                f.write(s.to_line())

    # -------- operaciones CRUD ---------------------------------------
    def create(self, student: Student) -> None:
        students = self._read_all()
        if any(s.student_id == student.student_id for s in students):
            raise ValueError("Ya existe un estudiante con ese ID.")
        students.append(student)
        self._write_all(students)

    def read_all(self) -> list[Student]:
        return self._read_all()

    def update(self, student: Student) -> None:
        students = self._read_all()
        for idx, s in enumerate(students):
            if s.student_id == student.student_id:
                students[idx] = student
                self._write_all(students)
                return
        raise KeyError("Estudiante no encontrado para actualizar.")

    def delete(self, student_id: str) -> None:
        students = self._read_all()
        new_students = [s for s in students if s.student_id != student_id]
        if len(new_students) == len(students):
            raise KeyError("Estudiante no encontrado para eliminar.")
        self._write_all(new_students)


# ---------------------------------------------------------------------
# 3.  INTERFAZ GRÁFICA
# ---------------------------------------------------------------------
class StudentApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Gestor de Estudiantes – Actividad 6")
        self.geometry("680x360")
        self.resizable(False, False)

        self.repo = StudentRepository()

        # ----- panel de entradas -------------------------------------
        frm_inputs = ttk.LabelFrame(self, text="Datos del estudiante")
        frm_inputs.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(frm_inputs, text="ID:").grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        ttk.Label(frm_inputs, text="Nombre:").grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)
        ttk.Label(frm_inputs, text="Edad:").grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        ttk.Label(frm_inputs, text="Correo:").grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)

        self.ent_id = ttk.Entry(frm_inputs, width=20)
        self.ent_name = ttk.Entry(frm_inputs, width=30)
        self.ent_age = ttk.Entry(frm_inputs, width=20)
        self.ent_email = ttk.Entry(frm_inputs, width=30)

        self.ent_id.grid(row=0, column=1, padx=5, pady=5)
        self.ent_name.grid(row=0, column=3, padx=5, pady=5)
        self.ent_age.grid(row=1, column=1, padx=5, pady=5)
        self.ent_email.grid(row=1, column=3, padx=5, pady=5)

        # ----- botones CRUD ------------------------------------------
        frm_btns = ttk.Frame(self)
        frm_btns.pack(side=tk.TOP, fill=tk.X, padx=10)

        ttk.Button(frm_btns, text="Create",           command=self.on_create).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frm_btns, text="Read / Refresh",   command=self.populate_table).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frm_btns, text="Update",           command=self.on_update).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(frm_btns, text="Delete",           command=self.on_delete).pack(side=tk.LEFT, padx=5, pady=5)

        # ----- tabla de resultados ----------------------------------
        columns = ("id", "name", "age", "email")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=8)
        for col, header in zip(columns, ("ID", "Nombre", "Edad", "Correo")):
            self.tree.heading(col, text=header)
            self.tree.column(col, anchor=tk.CENTER, stretch=False, width=160 if col != "name" else 180)
        self.tree.pack(side=tk.TOP, padx=10, pady=10)

        self.populate_table()

    # --------- helpers de GUI ----------------------------------------
    def _get_inputs(self) -> Student:
        try:
            return Student(
                student_id=self.ent_id.get().strip(),
                name=self.ent_name.get().strip(),
                age=int(self.ent_age.get().strip()),
                email=self.ent_email.get().strip(),
            )
        except ValueError:
            messagebox.showerror("Entrada inválida", "La edad debe ser un número entero.")
            raise

    def populate_table(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        for stu in self.repo.read_all():
            self.tree.insert("", tk.END, values=(stu.student_id, stu.name, stu.age, stu.email))

    # --------- callbacks de botones ----------------------------------
    def on_create(self) -> None:
        try:
            student = self._get_inputs()
            self.repo.create(student)
            self.populate_table()
            messagebox.showinfo("Éxito", "Estudiante registrado.")
        except Exception as exc:
            messagebox.showerror("Error al crear", str(exc))

    def on_update(self) -> None:
        try:
            student = self._get_inputs()
            self.repo.update(student)
            self.populate_table()
            messagebox.showinfo("Éxito", "Registro actualizado.")
        except Exception as exc:
            messagebox.showerror("Error al actualizar", str(exc))

    def on_delete(self) -> None:
        sid = self.ent_id.get().strip()
        if not sid:
            messagebox.showerror("Eliminar", "Debe especificar el ID del estudiante.")
            return
        try:
            self.repo.delete(sid)
            self.populate_table()
            messagebox.showinfo("Éxito", "Registro eliminado.")
        except Exception as exc:
            messagebox.showerror("Error al eliminar", str(exc))


# ---------------------------------------------------------------------
# 4.  EJECUCIÓN
# ---------------------------------------------------------------------
if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
