import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import serial
import serial.tools.list_ports
import threading
import time
from datetime import datetime

class SerialAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("串口调试助手")
        self.root.geometry("900x650")
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(True, True)

        # 现代化样式
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()

        self.ser = None
        self.running = False
        self.read_thread = None
        self.send_timer_id = None
        self.rx_count = 0
        self.tx_count = 0

        self.setup_ui()
        self.refresh_ports()
        self.update_status("串口未打开", False)

    def configure_styles(self):
        # 全局颜色
        self.bg_color = '#f5f5f5'
        self.fg_color = '#333333'
        self.accent_color = '#0078d4'
        self.danger_color = '#d32f2f'
        self.success_color = '#2e7d32'

        # 通用样式
        self.style.configure('.', background=self.bg_color, foreground=self.fg_color,
                             font=('Microsoft YaHei UI', 9))
        self.style.configure('TLabel', background=self.bg_color, foreground=self.fg_color)
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabelframe', background=self.bg_color, foreground=self.fg_color,
                             borderwidth=1, relief='solid')
        self.style.configure('TLabelframe.Label', font=('Microsoft YaHei UI', 9, 'bold'),
                             foreground=self.accent_color)

        # 按钮样式
        self.style.configure('TButton', font=('Microsoft YaHei UI', 9), borderwidth=1,
                             relief='flat', background='#e0e0e0', padding=(10, 5))
        self.style.map('TButton', background=[('active', '#d0d0d0')])

        # 主要按钮（打开/关闭串口）
        self.style.configure('Primary.TButton', background=self.accent_color,
                             foreground='white', font=('Microsoft YaHei UI', 9, 'bold'))
        self.style.map('Primary.TButton', background=[('active', '#005a9e')])

        # 组合框样式
        self.style.configure('TCombobox', padding=5, relief='flat', borderwidth=1)
        self.style.map('TCombobox', fieldbackground=[('readonly', 'white')])

        # 复选框样式
        self.style.configure('TCheckbutton', background=self.bg_color)

        # 计数栏标签样式
        self.style.configure('Count.TLabel', font=('Consolas', 9), foreground='#666666')

    def setup_ui(self):
        # 顶部标题栏（模拟）
        title_frame = ttk.Frame(self.root, padding=(15, 10))
        title_frame.pack(fill=tk.X)
        ttk.Label(title_frame, text="正点原子风格 · 串口调试助手", font=('Microsoft YaHei UI', 14, 'bold'),
                  foreground=self.accent_color).pack(side=tk.LEFT)

        # 主内容面板
        main_pw = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_pw.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        # 左侧设置面板
        left_frame = ttk.LabelFrame(main_pw, text="串口设置", padding=15)
        main_pw.add(left_frame, weight=0)

        # 间距统一
        pady = (0, 10)

        ttk.Label(left_frame, text="串口号:").grid(row=0, column=0, sticky=tk.W, pady=pady)
        self.port_var = tk.StringVar()
        self.port_combo = ttk.Combobox(left_frame, textvariable=self.port_var, width=14, state="readonly")
        self.port_combo.grid(row=0, column=1, pady=pady, padx=(10, 0))
        self.port_combo.bind("<Button-1>", lambda e: self.refresh_ports())

        ttk.Label(left_frame, text="波特率:").grid(row=1, column=0, sticky=tk.W, pady=pady)
        self.baud_var = tk.StringVar(value="115200")
        baud_combo = ttk.Combobox(left_frame, textvariable=self.baud_var, width=14,
                                  values=["300","1200","2400","4800","9600","14400","19200","38400",
                                          "57600","115200","230400","460800","921600"])
        baud_combo.grid(row=1, column=1, pady=pady, padx=(10, 0))

        ttk.Label(left_frame, text="数据位:").grid(row=2, column=0, sticky=tk.W, pady=pady)
        self.data_bit_var = tk.StringVar(value="8")
        data_combo = ttk.Combobox(left_frame, textvariable=self.data_bit_var, width=14,
                                  values=["5","6","7","8"], state="readonly")
        data_combo.grid(row=2, column=1, pady=pady, padx=(10, 0))

        ttk.Label(left_frame, text="停止位:").grid(row=3, column=0, sticky=tk.W, pady=pady)
        self.stop_bit_var = tk.StringVar(value="1")
        stop_combo = ttk.Combobox(left_frame, textvariable=self.stop_bit_var, width=14,
                                  values=["1","1.5","2"], state="readonly")
        stop_combo.grid(row=3, column=1, pady=pady, padx=(10, 0))

        ttk.Label(left_frame, text="校验位:").grid(row=4, column=0, sticky=tk.W, pady=pady)
        self.parity_var = tk.StringVar(value="无")
        parity_combo = ttk.Combobox(left_frame, textvariable=self.parity_var, width=14,
                                    values=["无","奇校验","偶校验","标记","空白"], state="readonly")
        parity_combo.grid(row=4, column=1, pady=pady, padx=(10, 0))

        ttk.Label(left_frame, text="流控:").grid(row=5, column=0, sticky=tk.W, pady=pady)
        self.flow_var = tk.StringVar(value="无")
        flow_combo = ttk.Combobox(left_frame, textvariable=self.flow_var, width=14,
                                  values=["无","RTS/CTS","XON/XOFF"], state="readonly")
        flow_combo.grid(row=5, column=1, pady=pady, padx=(10, 0))

        # 打开/关闭按钮（使用Primary样式）
        self.open_btn = ttk.Button(left_frame, text="打开串口", style='Primary.TButton', command=self.toggle_serial)
        self.open_btn.grid(row=6, column=0, columnspan=2, pady=(15, 10), sticky=tk.EW)

        # 状态指示（带颜色圆点）
        status_frame = ttk.Frame(left_frame)
        status_frame.grid(row=7, column=0, columnspan=2, pady=(5, 0))
        self.status_indicator = tk.Canvas(status_frame, width=10, height=10, bg=self.bg_color, highlightthickness=0)
        self.status_indicator.pack(side=tk.LEFT, padx=(0, 5))
        self.status_label = ttk.Label(status_frame, text="未连接", foreground=self.danger_color)
        self.status_label.pack(side=tk.LEFT)

        # 右侧收发区域
        right_frame = ttk.Frame(main_pw, padding=(10, 0))
        main_pw.add(right_frame, weight=1)

        # 接收区
        recv_frame = ttk.LabelFrame(right_frame, text="接收区", padding=10)
        recv_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        recv_option_frame = ttk.Frame(recv_frame)
        recv_option_frame.pack(fill=tk.X, pady=(0, 8))

        self.hex_show_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(recv_option_frame, text="HEX显示", variable=self.hex_show_var).pack(side=tk.LEFT, padx=5)
        self.timestamp_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(recv_option_frame, text="时间戳", variable=self.timestamp_var).pack(side=tk.LEFT, padx=5)
        self.auto_wrap_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(recv_option_frame, text="自动换行", variable=self.auto_wrap_var).pack(side=tk.LEFT, padx=5)

        ttk.Button(recv_option_frame, text="清空", command=self.clear_recv).pack(side=tk.RIGHT, padx=5)
        ttk.Button(recv_option_frame, text="保存", command=self.save_recv).pack(side=tk.RIGHT, padx=5)

        # 接收文本框（使用等宽字体，背景白色）
        self.recv_text = scrolledtext.ScrolledText(recv_frame, height=12, state=tk.DISABLED,
                                                   wrap=tk.WORD, font=('Consolas', 10),
                                                   bg='white', relief='flat', borderwidth=1)
        self.recv_text.pack(fill=tk.BOTH, expand=True)

        # 发送区
        send_frame = ttk.LabelFrame(right_frame, text="发送区", padding=10)
        send_frame.pack(fill=tk.BOTH, expand=True)

        send_option_frame = ttk.Frame(send_frame)
        send_option_frame.pack(fill=tk.X, pady=(0, 8))

        self.hex_send_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(send_option_frame, text="HEX发送", variable=self.hex_send_var).pack(side=tk.LEFT, padx=5)

        ttk.Label(send_option_frame, text="新行:").pack(side=tk.LEFT, padx=(10, 2))
        self.newline_var = tk.StringVar(value="\\r\\n")
        newline_combo = ttk.Combobox(send_option_frame, textvariable=self.newline_var, width=6,
                                     values=["无","\\r\\n","\\r","\\n"], state="readonly")
        newline_combo.pack(side=tk.LEFT, padx=2)

        self.timer_send_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(send_option_frame, text="定时发送", variable=self.timer_send_var,
                        command=self.toggle_timer_send).pack(side=tk.LEFT, padx=(10, 5))
        ttk.Label(send_option_frame, text="间隔(ms):").pack(side=tk.LEFT, padx=2)
        self.interval_var = tk.StringVar(value="1000")
        ttk.Entry(send_option_frame, textvariable=self.interval_var, width=6).pack(side=tk.LEFT, padx=2)

        ttk.Button(send_option_frame, text="发送", command=self.send_data).pack(side=tk.RIGHT, padx=5)
        ttk.Button(send_option_frame, text="清空", command=lambda: self.send_text.delete(1.0, tk.END)).pack(side=tk.RIGHT, padx=5)

        # 发送文本框
        self.send_text = scrolledtext.ScrolledText(send_frame, height=8, wrap=tk.WORD,
                                                   font=('Consolas', 10), bg='white',
                                                   relief='flat', borderwidth=1)
        self.send_text.pack(fill=tk.BOTH, expand=True)

        # 底部状态栏
        status_bar = ttk.Frame(right_frame)
        status_bar.pack(fill=tk.X, pady=(10, 0))
        self.rx_label = ttk.Label(status_bar, text="RX: 0 字节", style='Count.TLabel')
        self.rx_label.pack(side=tk.LEFT, padx=10)
        self.tx_label = ttk.Label(status_bar, text="TX: 0 字节", style='Count.TLabel')
        self.tx_label.pack(side=tk.LEFT, padx=10)

        # 分隔线
        ttk.Separator(right_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=(5, 0))

    # ---------- 串口操作 ----------
    def refresh_ports(self):
        ports = serial.tools.list_ports.comports()
        port_list = [p.device for p in ports]
        self.port_combo['values'] = port_list
        if port_list and not self.port_var.get():
            self.port_var.set(port_list[0])

    def toggle_serial(self):
        if self.ser and self.ser.is_open:
            self.close_serial()
        else:
            self.open_serial()

    def open_serial(self):
        port = self.port_var.get()
        if not port:
            messagebox.showerror("错误", "请选择串口")
            return
        try:
            baud = int(self.baud_var.get())
            data_bits = int(self.data_bit_var.get())
            stop_bits_map = {"1": serial.STOPBITS_ONE, "1.5": serial.STOPBITS_ONE_POINT_FIVE, "2": serial.STOPBITS_TWO}
            stop_bits = stop_bits_map[self.stop_bit_var.get()]
            parity_map = {"无": serial.PARITY_NONE, "奇校验": serial.PARITY_ODD, "偶校验": serial.PARITY_EVEN,
                          "标记": serial.PARITY_MARK, "空白": serial.PARITY_SPACE}
            parity = parity_map[self.parity_var.get()]
            flow_map = {"无": False, "RTS/CTS": 'rtscts', "XON/XOFF": 'xonxoff'}
            flow = flow_map[self.flow_var.get()]
            timeout = 0.1

            self.ser = serial.Serial(port=port, baudrate=baud, bytesize=data_bits,
                                     stopbits=stop_bits, parity=parity,
                                     timeout=timeout, xonxoff=(flow=='xonxoff'),
                                     rtscts=(flow=='rtscts'))
            self.running = True
            self.open_btn.config(text="关闭串口", style='Primary.TButton')  # 保持主按钮样式
            self.update_status(f"已连接 {port} @ {baud}", True)
            self.read_thread = threading.Thread(target=self.read_from_serial, daemon=True)
            self.read_thread.start()
        except Exception as e:
            messagebox.showerror("串口错误", str(e))

    def close_serial(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.open_btn.config(text="打开串口", style='Primary.TButton')
        self.update_status("未连接", False)
        self.stop_timer_send()

    def read_from_serial(self):
        while self.running and self.ser and self.ser.is_open:
            try:
                if self.ser.in_waiting:
                    data = self.ser.read(self.ser.in_waiting)
                    self.rx_count += len(data)
                    self.display_data(data)
                    self.update_rx_count()
            except serial.SerialException:
                self.root.after(0, self.handle_serial_error)
                break
            except Exception:
                break
            time.sleep(0.01)
        if self.running:
            self.root.after(0, self.close_serial)

    def handle_serial_error(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.running = False
        self.open_btn.config(text="打开串口", style='Primary.TButton')
        self.update_status("异常断开", False)
        messagebox.showerror("错误", "串口连接意外断开，请检查硬件连接。")

    def display_data(self, data):
        def _update():
            if self.hex_show_var.get():
                text = ' '.join(f'{b:02X}' for b in data)
            else:
                try:
                    text = data.decode('utf-8', errors='replace')
                except:
                    text = str(data)
            if self.timestamp_var.get():
                timestamp = datetime.now().strftime("[%H:%M:%S.%f] ")[:-4] + " "
                text = timestamp + text
            if self.auto_wrap_var.get() and not self.hex_show_var.get():
                text += '\n'
            self.recv_text.configure(state=tk.NORMAL)
            self.recv_text.insert(tk.END, text)
            self.recv_text.see(tk.END)
            self.recv_text.configure(state=tk.DISABLED)
        self.root.after(0, _update)

    # ---------- 发送 ----------
    def send_data(self):
        if not self.ser or not self.ser.is_open:
            messagebox.showwarning("提示", "串口未打开")
            return
        raw = self.send_text.get("1.0", tk.END).rstrip('\n')
        if not raw:
            return
        try:
            if self.hex_send_var.get():
                hex_str = raw.replace(' ', '').replace('\n', '').replace('\r', '')
                if len(hex_str) % 2 != 0:
                    messagebox.showerror("错误", "HEX发送格式错误，请确保每个字节用两个十六进制字符表示")
                    return
                data = bytes.fromhex(hex_str)
            else:
                data = raw.encode('utf-8')
            newline_map = {"无": b"", "\\r\\n": b"\r\n", "\\r": b"\r", "\\n": b"\n"}
            data += newline_map[self.newline_var.get()]
            self.ser.write(data)
            self.tx_count += len(data)
            self.update_tx_count()
        except ValueError:
            messagebox.showerror("错误", "HEX发送字符串包含无效字符")
        except Exception as e:
            messagebox.showerror("发送失败", str(e))

    # ---------- 定时发送 ----------
    def toggle_timer_send(self):
        if self.timer_send_var.get():
            self.start_timer_send()
        else:
            self.stop_timer_send()

    def start_timer_send(self):
        if not self.ser or not self.ser.is_open:
            self.timer_send_var.set(False)
            messagebox.showwarning("提示", "请先打开串口再启动定时发送")
            return
        try:
            interval = int(self.interval_var.get())
            if interval <= 0:
                raise ValueError
        except:
            messagebox.showerror("错误", "定时间隔必须为正整数(ms)")
            self.timer_send_var.set(False)
            return
        self.stop_timer_send()
        self._timer_send(interval)

    def _timer_send(self, interval):
        if not self.timer_send_var.get():
            return
        self.send_data()
        self.send_timer_id = self.root.after(interval, lambda: self._timer_send(interval))

    def stop_timer_send(self):
        if self.send_timer_id:
            self.root.after_cancel(self.send_timer_id)
            self.send_timer_id = None
        self.timer_send_var.set(False)

    # ---------- 辅助功能 ----------
    def clear_recv(self):
        self.recv_text.configure(state=tk.NORMAL)
        self.recv_text.delete(1.0, tk.END)
        self.recv_text.configure(state=tk.DISABLED)
        self.rx_count = 0
        self.update_rx_count()

    def save_recv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.recv_text.get("1.0", tk.END))
                messagebox.showinfo("成功", "数据已保存")
            except Exception as e:
                messagebox.showerror("保存失败", str(e))

    def update_status(self, msg, connected):
        color = self.success_color if connected else self.danger_color
        self.status_label.config(text=msg, foreground=color)
        # 更新圆点颜色
        self.status_indicator.delete("all")
        r = 4
        x, y = 5, 5
        self.status_indicator.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color)

    def update_rx_count(self):
        self.rx_label.config(text=f"RX: {self.rx_count} 字节")

    def update_tx_count(self):
        self.tx_label.config(text=f"TX: {self.tx_count} 字节")

    def on_closing(self):
        self.running = False
        self.stop_timer_send()
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialAssistant(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()