from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, TransactionGroup
doc = __revit__.ActiveUIDocument.Document
sheets_collector=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

tg = TransactionGroup(doc, "Update and Delete")
tg.Start()
t=Transaction(doc,"Update Sheet Parameters")
t.Start()

for sheet in sheets_collector:
    custom_param=sheet.LookupParameter("Drawing Scale")
    if custom_param.AsString() == "1:200":
        custom_param.Set("1:200@A3")
    elif custom_param.AsString() == "1:100":
        custom_param.Set("1:100@A3")
    elif custom_param.AsString() == "1:50":
        custom_param.Set("1:50@A3")
    elif custom_param.AsString() == "1:20":
        custom_param.Set("1:20@A3")
    elif custom_param.AsString() == "1:10":
        custom_param.Set("1:10@A3")
t.Commit()

tg.Assimilate()