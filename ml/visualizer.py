import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from ml.loader import get_full_dataset
import seaborn as sns
import io
import base64
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def cechy(vol, sulfur, chlor, sulph):
    df = get_full_dataset()
    # Mapowanie kolorów HEX
    hex_palette = {0:'#d9dcd6', 1: "#8d0d3e"}

    # Wykresy
    plt.figure(figsize=(12, 5))

    # Wykres 1
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='VolatileAcidity', y='TotalSulfurDioxide',
                    hue='ColorBin', palette=hex_palette, alpha=0.6, edgecolor=None)
    plt.scatter(vol, sulfur, color='black', marker='+', s=200, label='Twoje dane')
    plt.xlabel("VolatileAcidity")
    plt.ylabel("TotalSulfurDioxide")
    plt.title("Kwasowość lotna vs Całkowita zawartość dwutlenku siarki")
    plt.legend()

    # Wykres 2
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df, x='Chlorides', y='Sulphates',
                    hue='ColorBin', palette=hex_palette, alpha=0.6, edgecolor=None)
    plt.scatter(chlor, sulph, color='black', marker='+', s=200, label='Twoje dane')
    plt.xlabel("Chlorides")
    plt.ylabel("Sulphates")
    plt.title("Chlorki vs Siarczany")
    plt.legend()

    fig = plt.gcf()
    return convert_to_base64(fig)


def plot_conf_matrix(y_true, y_pred, model_name=None):
    cm = confusion_matrix(y_true, y_pred)

    cmap = "Blues"
    if model_name == "random_forest":
        cmap = "PuBuGn"
    elif model_name == "knn":
        cmap = "YlOrBr"
    elif model_name == "svm":
        cmap = "YlGn"    

    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap=cmap, ax=ax)
    ax.set_xlabel('Predykcja')
    ax.set_ylabel('Rzeczywista')
    ax.set_title('Macierz pomyłek')
    return convert_to_base64(fig)

def generate_classification_report(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    print(f'Accuracy: {accuracy * 100:.2f}%') #dodac do aplikacji w raporcie
    report = classification_report(y_true, y_pred, target_names=['Białe', 'Czerwone'])
    return report

def convert_to_base64(fig):
    buf = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format='png')
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return encoded