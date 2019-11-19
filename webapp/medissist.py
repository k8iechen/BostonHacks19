from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  def PatientName_copy_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def PatientDOBtextBox_copy_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
  def file_loader_1_change (self, file, **event_args):
    # This method is called when a new file is loaded into this FileLoader
    x = anvil.server.call("get_file",file)
    img1.source = file
    
  def firstApproveBtn_click(self, **event_args):
    """This method is called when the button is clicked"""

    self.name_P.text = "Name: " + self.PatientName.text
    
    z = self.date_picker_1.date
    
    self.Pdob_field.text = "DOB: " + z.strftime('%m/%d/%Y')
    x = self.PsymptomDescription.text
    y = self.label_2.text
    if self.file_loader_1.file:
      d = self.file_loader_1.file.get_bytes()
      
      if "Syphilis" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Capillary whole blood: Combined antibodies to T. pallidum and to HIV-1/2 (anti-HIV)"
        self.button_2.text = "Capillary whole blood: Antibodies to Treponema pallidum"
        self.button_2.visible = True
        self.button_1.visible = True
      elif "HIV" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Combined HIV antibody"
        self.button_2.text = "p24 antigen (antiHIV/p24 Ag) test"
        self.button_2.visible = True
        self.button_1.visible = True
      elif "Tuberculosis" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Microscopy for Mycobacterium Tuberculosis Bacteria"
        self.button_2.text = "Intradermal Skin Test (TST) for Immune Response"
        self.button_2.visible = True
        self.button_1.visible = True
    else:
      
      if "Syphilis" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Capillary whole blood: Combined antibodies to T. pallidum and to HIV-1/2 (anti-HIV)"
        self.button_2.text = "Capillary whole blood: Antibodies to Treponema pallidum"
        self.button_2.visible = True
        self.button_1.visible = True
      if "HIV" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Combined HIV antibody"
        self.button_2.text = "p24 antigen (antiHIV/p24 Ag) test"
        self.button_2.visible = True
        self.button_1.visible = True
      if "Tuberculosis" in y:
        self.Pos_symptons.text = "Suggested tests: "
        self.button_1.text = "Microscopy for Mycobacterium Tuberculosis Bacteria"
        self.button_2.text = "Intradermal Skin Test (TST) for Immune Response"
        self.button_2.visible = True
        self.button_1.visible = True
    
    self.card_2.visible = True
    pass

  
  def button_1_click(self, **event_args):
   
    """This method is called when the button is clicked"""
    y = self.label_2.text
    #y = self.file_loader_1.file.get_bytes()
    if "Syphilis" in y:
      self.btn_one_out.text = "\nCapillary whole blood: Combined antibodies to T. pallidum and to HIV-1/2 (anti-HIV)"
      
    elif "HIV" in y:
      self.btn_one_out.text = "\nCombined HIV antibody"
      
    elif "Tuberculosis" in y:
      self.btn_one_out.text = "\nMicroscopy for Mycobacterium Tuberculosis Bacteria"
    
    self.button_1.visible = False
    pass
  
  def button_2_click(self, **event_args):
    y = self.label_2.text
    #y = self.file_loader_1.file.get_bytes()
    """This method is called when the button is clicked"""
    if "Syphilis" in y:
      self.btn_one_out.text += "\nCapillary whole blood: Antibodies to Treponema pallidum"
      
    elif "HIV" in y:
      self.btn_one_out.text += "\np24 antigen (antiHIV/p24 Ag) test"
      
    elif "Tuberculosis" in y:
      self.btn_one_out.text += "\nIntradermal Skin Test (TST) for Immune Response"
    self.button_2.visible = False
    pass
  
  def firstApproveBtn_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.name_P_copy.text = "Name: " + self.PatientName.text
    
    z = self.date_picker_1.date
    x = self.PsymptomDescription.text
    self.Pdob_field_copy.text = "DOB: " + z.strftime('%m/%d/%Y')
    self.Pos_symptons_copy.text = "Symptons: " + x
    
    self.test_output.text = self.btn_one_out.text
    self.card_2_copy.visible = True
    pass
  
    

  def firstApproveBtn_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.card_3.visible = True
   # people_called_dave = URLMedia("https://drive.google.com/file/d/1R6QYaOlRuCrBvkbF8q40ri6p6Zs8wbG3/view?usp=sharing")
    #download(people_called_dave)
    
    pass

  def PsymptomDescription_change(self, **event_args):
    """This method is called when the text in this text area is edited"""

    pass









  


