#pragma once

#include <QEvent>

void DemoQEvent() {
    QEvent e{QEvent::Type::ActionChanged};
}