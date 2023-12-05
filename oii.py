import cv2

# Inicializar a câmera
cap = cv2.VideoCapture(0)

# Verificar se a câmera foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

# Loop para capturar frames da câmera
while True:
    # Capturar um frame da câmera
    ret, frame = cap.read()

    # Verificar se o frame foi capturado corretamente
    if not ret:
        print("Erro ao capturar o frame.")
        break

    # Exibir o frame em uma janela
    cv2.imshow('Câmera', frame)

    # Verificar se o usuário pressionou a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
