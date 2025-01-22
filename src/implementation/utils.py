import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(context='paper', style='ticks', palette='deep', color_codes=True)
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['figure.dpi'] = 100
# plt.style.use('https://pltstyle.s3.eu-west-1.amazonaws.com/zinc.mplstyle')


def roc_plot(y_true, y_val_proba):
    fpr, tpr, _ = roc_curve(y_true, y_val_proba)
    roc_auc = roc_auc_score(y_true, y_val_proba)
    plt.figure()
    plt.plot(fpr, tpr, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='best')
    plt.show()

def precision_recall_plot(y_true, y_val_proba):
    precision, recall, thresholds_pr = precision_recall_curve(y_true, y_val_proba)
    plt.figure()
    plt.plot(thresholds_pr, precision[:-1], 'b--', label='Precision')
    plt.plot(thresholds_pr, recall[:-1], 'g-', label='Recall')
    plt.xlabel('Threshold')
    plt.ylabel('Score')
    plt.title('Precision-Recall Curve')
    plt.legend(loc='best')
    plt.show()

def table_report(y_true, y_pred):
    report_dict = classification_report(y_true, y_pred, output_dict=True, target_names=['ham', 'spam'])
    report_dict.update({"accuracy": {"precision": None, "recall": None, "f1-score": report_dict["accuracy"], "support": report_dict['macro avg']['support']}})
    report_df = pd.DataFrame(report_dict).T
    report_df['support'] = report_df['support'].astype(int)
    # Format non null float number to rounded percentage
    report_df = report_df.map(lambda x: f"{round(x * 100, 2):.2f}%" if isinstance(x, float) and not np.isnan(x) else x) 
    report_df = report_df.fillna('')
    display(report_df)