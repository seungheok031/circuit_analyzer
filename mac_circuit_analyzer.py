import tkinter as tk
from tkinter import ttk
import math

class CircuitAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("전기회로 해석 프로그램")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # 스타일 설정
        self.style = ttk.Style()
        self.style.configure('TButton', padding=10, font=('Helvetica', 12))
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TEntry', padding=5)
        
        # 메인 프레임
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 모드 선택 버튼
        self.mode_frame = ttk.Frame(self.main_frame)
        self.mode_frame.pack(fill=tk.X, pady=10)
        
        self.modes = {
            "직렬 저항": self.create_series_resistance_frame,
            "병렬 저항": self.create_parallel_resistance_frame,
            "전압 분배": self.create_voltage_divider_frame,
            "전류 분배": self.create_current_divider_frame,
            "옴의 법칙": self.create_ohms_law_frame,
            "오차율": self.create_error_rate_frame
        }
        
        for mode in self.modes:
            btn = ttk.Button(self.mode_frame, text=mode, 
                           command=lambda m=mode: self.switch_mode(m))
            btn.pack(side=tk.LEFT, padx=5)
        
        # 계산 프레임
        self.calc_frame = ttk.Frame(self.main_frame)
        self.calc_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 초기 모드 설정
        self.current_mode = "직렬 저항"
        self.switch_mode(self.current_mode)
        
    def switch_mode(self, mode):
        # 이전 프레임 제거
        for widget in self.calc_frame.winfo_children():
            widget.destroy()
        
        # 새로운 모드 프레임 생성
        self.modes[mode]()
        self.current_mode = mode
    
    def create_series_resistance_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="직렬 저항 계산", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="저항값 (쉼표로 구분):").pack()
        self.series_input = ttk.Entry(input_frame, width=50)
        self.series_input.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_series).pack(pady=10)
        
        self.series_result = ttk.Label(frame, text="")
        self.series_result.pack(pady=10)
    
    def create_parallel_resistance_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="병렬 저항 계산", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="저항값 (쉼표로 구분):").pack()
        self.parallel_input = ttk.Entry(input_frame, width=50)
        self.parallel_input.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_parallel).pack(pady=10)
        
        self.parallel_result = ttk.Label(frame, text="")
        self.parallel_result.pack(pady=10)
    
    def create_voltage_divider_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="전압 분배 법칙", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="입력 전압 (V):").pack()
        self.voltage_input = ttk.Entry(input_frame)
        self.voltage_input.pack(pady=5)
        
        ttk.Label(input_frame, text="R1 (Ω):").pack()
        self.r1_input = ttk.Entry(input_frame)
        self.r1_input.pack(pady=5)
        
        ttk.Label(input_frame, text="R2 (Ω):").pack()
        self.r2_input = ttk.Entry(input_frame)
        self.r2_input.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_voltage_divider).pack(pady=10)
        
        self.voltage_divider_result = ttk.Label(frame, text="")
        self.voltage_divider_result.pack(pady=10)
    
    def create_current_divider_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="전류 분배 법칙", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="총 전류 (A):").pack()
        self.current_input = ttk.Entry(input_frame)
        self.current_input.pack(pady=5)
        
        ttk.Label(input_frame, text="R1 (Ω):").pack()
        self.current_r1_input = ttk.Entry(input_frame)
        self.current_r1_input.pack(pady=5)
        
        ttk.Label(input_frame, text="R2 (Ω):").pack()
        self.current_r2_input = ttk.Entry(input_frame)
        self.current_r2_input.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_current_divider).pack(pady=10)
        
        self.current_divider_result = ttk.Label(frame, text="")
        self.current_divider_result.pack(pady=10)
    
    def create_ohms_law_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="옴의 법칙", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="전압 (V):").pack()
        self.ohms_voltage = ttk.Entry(input_frame)
        self.ohms_voltage.pack(pady=5)
        
        ttk.Label(input_frame, text="전류 (A):").pack()
        self.ohms_current = ttk.Entry(input_frame)
        self.ohms_current.pack(pady=5)
        
        ttk.Label(input_frame, text="저항 (Ω):").pack()
        self.ohms_resistance = ttk.Entry(input_frame)
        self.ohms_resistance.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_ohms_law).pack(pady=10)
        
        self.ohms_law_result = ttk.Label(frame, text="")
        self.ohms_law_result.pack(pady=10)
    
    def create_error_rate_frame(self):
        frame = ttk.Frame(self.calc_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="오차율 계산", font=('Helvetica', 16, 'bold')).pack(pady=10)
        
        input_frame = ttk.Frame(frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="이론값:").pack()
        self.theoretical_input = ttk.Entry(input_frame)
        self.theoretical_input.pack(pady=5)
        
        ttk.Label(input_frame, text="측정값:").pack()
        self.measured_input = ttk.Entry(input_frame)
        self.measured_input.pack(pady=5)
        
        ttk.Button(frame, text="계산", 
                  command=self.calculate_error_rate).pack(pady=10)
        
        self.error_rate_result = ttk.Label(frame, text="")
        self.error_rate_result.pack(pady=10)
    
    def calculate_series(self):
        try:
            resistors = [float(r.strip()) for r in self.series_input.get().split(',')]
            total = sum(resistors)
            self.series_result.config(text=f"총 저항: {total} Ω")
        except ValueError:
            self.series_result.config(text="올바른 값을 입력하세요")
    
    def calculate_parallel(self):
        try:
            resistors = [float(r.strip()) for r in self.parallel_input.get().split(',')]
            reciprocal_sum = sum(1/r for r in resistors)
            total = 1/reciprocal_sum if reciprocal_sum != 0 else 0
            self.parallel_result.config(text=f"총 저항: {total:.2f} Ω")
        except ValueError:
            self.parallel_result.config(text="올바른 값을 입력하세요")
    
    def calculate_voltage_divider(self):
        try:
            v_in = float(self.voltage_input.get())
            r1 = float(self.r1_input.get())
            r2 = float(self.r2_input.get())
            v_out = v_in * (r2 / (r1 + r2))
            self.voltage_divider_result.config(text=f"출력 전압: {v_out:.2f} V")
        except ValueError:
            self.voltage_divider_result.config(text="올바른 값을 입력하세요")
    
    def calculate_current_divider(self):
        try:
            i_total = float(self.current_input.get())
            r1 = float(self.current_r1_input.get())
            r2 = float(self.current_r2_input.get())
            i1 = i_total * (r2 / (r1 + r2))
            i2 = i_total * (r1 / (r1 + r2))
            self.current_divider_result.config(
                text=f"R1 전류: {i1:.4f} A\nR2 전류: {i2:.4f} A"
            )
        except ValueError:
            self.current_divider_result.config(text="올바른 값을 입력하세요")
    
    def calculate_ohms_law(self):
        try:
            voltage = self.ohms_voltage.get()
            current = self.ohms_current.get()
            resistance = self.ohms_resistance.get()
            
            if voltage and current:
                r = float(voltage) / float(current)
                self.ohms_law_result.config(text=f"저항: {r:.2f} Ω")
            elif voltage and resistance:
                i = float(voltage) / float(resistance)
                self.ohms_law_result.config(text=f"전류: {i:.4f} A")
            elif current and resistance:
                v = float(current) * float(resistance)
                self.ohms_law_result.config(text=f"전압: {v:.2f} V")
            else:
                self.ohms_law_result.config(text="두 개의 값을 입력하세요")
        except ValueError:
            self.ohms_law_result.config(text="올바른 값을 입력하세요")
    
    def calculate_error_rate(self):
        try:
            theoretical = float(self.theoretical_input.get())
            measured = float(self.measured_input.get())
            if theoretical == 0:
                error_rate = 0
            else:
                error_rate = abs((measured - theoretical) / theoretical) * 100
            self.error_rate_result.config(text=f"오차율: {error_rate:.2f}%")
        except ValueError:
            self.error_rate_result.config(text="올바른 값을 입력하세요")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CircuitAnalyzer()
    app.run() 